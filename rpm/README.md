To build image for RHEL-7, RHEL-8 need define variables `repo_owner`, `base_image`, `image_tag`, `RHEL_USERNAME`, `RHEL_PASSWORD` and
then start build image like

```sh
export repo_owner=example
export base_image=rhel-9
export RHEL_USERNAME=${your_username}
export RHEL_PASSWORD=${your_password}
export platform=x86_64
docker buildx build \
    --platform linux/${platform} \
    --secret id=RHEL_USERNAME,env=RHEL_USERNAME \
    --secret id=RHEL_PASSWORD,env=RHEL_PASSWORD \
    --build-arg base_image="registry.redhat.io/ubi9/ubi:latest" \
    -t ${repo_owner}/kamailio-builder:${base_image} .
```

To build image for other dist need to define environment variables `repo_owner`, `base_image`, `image_tag` and then start build image like

```sh
export repo_owner=example
export base_image=fedora-42
export platform=x86_64
docker buildx build \
    --platform linux/${platform} \
    --build-arg base_image=${base_image} \
    -t ${repo_owner}/kamailio-builder:${base_image} .
```

To build for CentOS Stream
```sh
export repo_owner=example
export base_image=centos-10
export platform=x86_64
docker buildx build \
    --platform linux/${platform} \
    --build-arg base_image="quay.io/centos/centos:stream10" \
    -t ${repo_owner}/kamailio-builder:${base_image} .
```

Suported dist

| dist                | version | arch                          |
|---------------------|---------|--------------------------------
| rhel                | 10      |x86_64, aarch64, s390x         |
| rhel                | 9       |x86_64, aarch64                |
| rhel                | 8       |x86_64, aarch64                |
| centos              | 10      |x86_64, aarch64, s390x, ppc64le|
| centos              | 9       |x86_64, aarch64, s390x, ppc64le|
| centos              | 8       |x86_64, aarch64, s390x         |
| rocky               | 9       |x86_64, aarch64, s390x, ppc64le|
| fedora              | 42      |x86_64, aarch64, s390x, ppc64le|
| fedora              | 41      |x86_64, aarch64, s390x, ppc64le|
