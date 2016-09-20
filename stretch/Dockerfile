FROM debian:stretch

MAINTAINER Victor Seva <linuxmaniac@torreviejawireless.org>

# Important! Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like 'apt-get update' won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT 2016-09-20

# avoid httpredir errors
RUN sed -i 's/httpredir/ftp.us/g' /etc/apt/sources.list

RUN rm -rf /var/lib/apt/lists/* && apt-get update
RUN apt-get install --assume-yes  clang-3.7 pbuilder 

VOLUME /code

RUN mkdir -p /usr/local/src/pkg
COPY debian /usr/local/src/pkg/debian

# get build dependences
RUN cd /usr/local/src/pkg/ && /usr/lib/pbuilder/pbuilder-satisfydepends-experimental

# clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
