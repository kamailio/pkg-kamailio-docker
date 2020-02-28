To build image for RHEL-7, RHEL-8 need define variables `repo_owner`, `base_image`, `image_tag`, `rhel_username`, `rhel_password` and
then start build image like

```sh
export repo_owner=safarov
export base_image=rhel
export image_tag=8
export rhel_username=${your_username}
export rhel_password=${your_password}
docker build \
    --build-arg base_image=registry.redhat.io/ubi${image_tag} \
    --build-arg image_tag=latest \
    --build-arg rhel_username=${rhel_username} \
    --build-arg rhel_password=${rhel_password} \
    -t ${repo_owner}/pkg-kamailio-docker:${base_image}-${image_tag} .
```

To build image for other rpm dists need to define environement variables `repo_owner`, `base_image`, `image_tag` and then start build image like

```sh
export repo_owner=safarov
export base_image=fedora
export image_tag=31
docker build \
    --build-arg base_image=${base_image} \
    --build-arg image_tag=${image_tag} \
    -t ${repo_owner}/pkg-kamailio-docker:${base_image}-${image_tag} .
```
