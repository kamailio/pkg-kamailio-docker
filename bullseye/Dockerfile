FROM debian:bullseye

MAINTAINER Victor Seva <linuxmaniac@torreviejawireless.org>

# Important! Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like 'apt-get update' won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT 2023-03-03

# avoid httpredir errors
RUN find /etc/apt -name '*.list' -exec sed -i 's/httpredir/deb/g' {} \;

RUN rm -rf /var/lib/apt/lists/* && apt-get update
RUN echo 'MIRRORSITE="http://deb.debian.org/debian"' > /etc/pbuilderrc
RUN apt-get install -qq --assume-yes  clang-11 pbuilder 

VOLUME /code

RUN mkdir -p /usr/local/src/pkg
COPY debian /usr/local/src/pkg/debian

# get build dependences
RUN cd /usr/local/src/pkg/ && /usr/lib/pbuilder/pbuilder-satisfydepends-experimental

# clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
