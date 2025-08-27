FROM debian:sid
LABEL org.opencontainers.image.authors="Victor Seva <linuxmaniac@torreviejawireless.org>"

# Important! Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like 'apt-get update' won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT="2025-08-27"

RUN rm -rf /var/lib/apt/lists/* && apt-get update
RUN echo MIRRORSITE=http://deb.debian.org/debian > /etc/pbuilderrc
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq --assume-yes  clang pbuilder cmake

VOLUME /code

RUN mkdir -p /usr/local/src/pkg
COPY debian /usr/local/src/pkg/debian

# get build dependences
RUN cd /usr/local/src/pkg/ && /usr/lib/pbuilder/pbuilder-satisfydepends-experimental

# clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /code
