FROM debian:squeeze

MAINTAINER Victor Seva <linuxmaniac@torreviejawireless.org>

# Important! Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like 'apt-get update' won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT 2018-11-19

RUN echo "deb http://archive.debian.org/debian squeeze main" > /etc/apt/sources.list;     echo "deb http://archive.debian.org/debian squeeze-lts main" >> /etc/apt/sources.list ;     echo "Acquire::Check-Valid-Until false;" >> /etc/apt/apt.conf

RUN rm -rf /var/lib/apt/lists/* && apt-get update
RUN apt-get install --assume-yes  pbuilder 

VOLUME /code

RUN mkdir -p /usr/local/src/pkg
COPY debian /usr/local/src/pkg/debian

# get build dependences
RUN cd /usr/local/src/pkg/ && /usr/lib/pbuilder/pbuilder-satisfydepends-experimental

# clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
