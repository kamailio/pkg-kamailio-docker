ARG base_image="quay.io/centos/centos:stream10"

FROM ${base_image}
ARG base_image

COPY rpm_extra_specs /rpm_extra_specs/
COPY get_build_env.sh /get_build_env.sh

RUN --mount=type=secret,id=RHEL_USERNAME,env=RHEL_USERNAME \
    --mount=type=secret,id=RHEL_PASSWORD,env=RHEL_PASSWORD \
    /get_build_env.sh
