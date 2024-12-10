#!/bin/bash

create_dockerfile() {
  rm -rf "${dist}"
  mkdir -p "${dist}"
  cp -r "src/pkg/kamailio/deb/${dist}/" "${dist}/debian/"
  cat >"${dist}"/Dockerfile <<EOF
FROM ${docker_tag}
LABEL org.opencontainers.image.authors="Victor Seva <linuxmaniac@torreviejawireless.org>"

# Important! Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like 'apt-get update' won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT="${DATE}"

EOF

if ${archived} ; then
cat >>"${dist}"/Dockerfile <<EOF
# fix repositories
${RULE}
EOF
fi

cat >>"${dist}"/Dockerfile <<EOF
RUN rm -rf /var/lib/apt/lists/* && apt-get update
RUN echo MIRRORSITE=http://${MIRROR}/${base} > /etc/pbuilderrc
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq --assume-yes ${CLANG} pbuilder ${TOOLS}

VOLUME /code

RUN mkdir -p /usr/local/src/pkg
COPY debian /usr/local/src/pkg/debian

# get build dependences
RUN cd /usr/local/src/pkg/ && /usr/lib/pbuilder/pbuilder-satisfydepends-experimental

# clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /code
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
  noble|jammy|focal|bionic|xenial|trusty|precise) base=ubuntu ;;
  squeeze|wheezy|jessie|stretch|buster|bullseye|bookworm|sid) base=debian ;;
  *)
    echo "ERROR: no ${dist} base supported"
    exit 1
    ;;
esac

case ${dist} in
  squeeze|wheezy|jessie|stretch) docker_tag=${base}/eol:${dist} ;;
  *) docker_tag=${base}:${dist} ;;
esac

case ${base} in
  ubuntu) MIRROR=archive.ubuntu.com ;;
  debian) MIRROR=deb.debian.org ;;
esac

archived=false
case ${dist} in
  precise)
    archived=true ; MIRROR=old-release.ubuntu.com
    RULE="RUN sed -i -e 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list"
    ;;
  squeeze|wheezy|jessie|stretch)
    archived=true ; MIRROR=archive.debian.org
    RULE="RUN sed -i -e 's/deb.debian.org/archive.debian.org/g' -e '/security.debian.org/d' -e '/${dist}-updates/d' /etc/apt/sources.list"
    ;;
esac

case ${dist} in
	squeeze|wheezy) CLANG="" ;;
	jessie)	        CLANG=" clang-3.5" ;;
	stretch)        CLANG=" clang-3.8" ;;
	buster)         CLANG=" clang-7" ;;
	bullseye)       CLANG=" clang-11" ;;
  *)              CLANG=" clang" ;;
esac

TOOLS=cmake

create_dockerfile
