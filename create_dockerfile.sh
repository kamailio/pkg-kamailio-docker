#!/bin/bash

create_dockerfile() {
  rm -rf "${dist}"
  mkdir -p "${dist}"
  cp -r "src/pkg/kamailio/deb/${dist}/" "${dist}/debian/"
  cat >"${dist}"/Dockerfile <<EOF
FROM ${base}:${dist}

MAINTAINER Victor Seva <linuxmaniac@torreviejawireless.org>

# Important! Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like 'apt-get update' won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT ${DATE}

EOF

if [ "${base}" = "debian" ] ; then
cat >>"${dist}"/Dockerfile <<EOF
# avoid httpredir errors
RUN sed -i 's/httpredir/deb/g' /etc/apt/sources.list

EOF
fi

cat >>"${dist}"/Dockerfile <<EOF
RUN rm -rf /var/lib/apt/lists/* && apt-get update
RUN apt-get install --assume-yes ${CLANG} pbuilder ${TOOLS}

VOLUME /code

RUN mkdir -p /usr/local/src/pkg
COPY debian /usr/local/src/pkg/debian

# get build dependences
RUN cd /usr/local/src/pkg/ && /usr/lib/pbuilder/pbuilder-satisfydepends-experimental

# clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
EOF
}

dist=${1:-sid}

DATE=$(date --rfc-3339=date)

if ! [ -d src ] ; then
  echo "src dir missing" >&2
	echo "Exec: git clone https://github.com/kamailio/kamailio.git src"
  exit 1
fi

if ! [ -d "src/pkg/kamailio/deb/${dist}/" ] ; then
	echo "ERROR: no ${dist} support"
	exit 1
fi

case ${dist} in
	squeeze|wheezy) CLANG="" ;;
	jessie)	        CLANG=" clang-3.5" ;;
	stretch)        CLANG=" clang-3.8" ;;
	sid|buster)     CLANG=" clang-7" ;;
esac

case ${dist} in
  bionic|xenial|trusty|precise) base=ubuntu ;;
  squeeze|wheezy|jessie) base=debian/eol ;;
  stretch|buster|sid) base=debian ;;
  *)
    echo "ERROR: no ${dist} base found"
    exit 1
    ;;
esac

create_dockerfile
