# Description

Docker Debian based Images with dependences installed ready to be used
to build Kamailio from sources

# Upgrade

You need the kamailio sources at _src_ so get them:

```
git clone https://github.com/kamailio/kamailio.git src
```

or refresh them:

```
cd src
git pull
```

and just
```
make
```

# build locally the image
for instance:
```
export DIST=stretch VERSION=dev
```
```
cd ${DIST}; docker build --tag=pkg-kamailio-docker:${VERSION}-${DIST} .
```

or pull the image from docker hub

```
docker pull kamailio/pkg-kamailio-docker:${VERSION}-${DIST}
```
# run container
```
docker run -i -t --rm -v src:/code:rw kamailio/pkg-kamailio-docker:${VESION}-${DIST} /bin/bash
```
