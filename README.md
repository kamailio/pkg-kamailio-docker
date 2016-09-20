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
make pull
```

and just
```
make
```

# build locally the image
```
cd ${DIST}; docker build --tag=pkg-kamailio-docker:${DIST} .
```

or pull the image from docker hub

```
docker pull kamailio/pkg-kamailio-docker:${DIST}
```
# run container
```
docker run -i -t --rm -v src:/code:rw kamailio/pkg-kamailio-docker:${DIST} /bin/bash
```
