# Ubuntu 20.04 (focal)
# https://hub.docker.com/_/ubuntu/?tab=tags&name=focal
ARG ROOT_CONTAINER=amr-registry.caas.intel.com/intelaa/ubuntu:20.04
# ARG ROOT_CONTAINER=ubuntu:20.04
FROM $ROOT_CONTAINER

LABEL maintainer="Omer Elezra <omer.elezra@intel.com>"

USER root
ENV PYTHON_VERSION=3.9
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --yes && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends \   
    sudo \
    curl \
    openssh-server \
    cifs-utils \
    wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
