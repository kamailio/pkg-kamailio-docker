FROM ubuntu:precise
LABEL org.opencontainers.image.authors="Victor Seva <linuxmaniac@torreviejawireless.org>"

# Important! Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like 'apt-get update' won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT="2024-08-27"

# fix repositories
RUN sed -i -e 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
RUN rm -rf /var/lib/apt/lists/* && apt-get update
RUN echo MIRRORSITE=http://old-release.ubuntu.com/ubuntu > /etc/pbuilderrc
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq --assume-yes  clang pbuilder 

VOLUME /code

RUN mkdir -p /usr/local/src/pkg
COPY debian /usr/local/src/pkg/debian

# get build dependences
RUN cd /usr/local/src/pkg/ && /usr/lib/pbuilder/pbuilder-satisfydepends-experimental

# clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /code
