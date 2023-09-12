FROM ubuntu:22.04

# GNU compiler
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        g++ \
        gcc \
        gfortran && \
    rm -rf /var/lib/apt/lists/*

# LLVM compiler
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        clang-15 \
        libomp-15-dev && \
    rm -rf /var/lib/apt/lists/*
RUN update-alternatives --install /usr/bin/clang clang $(which clang-15) 30 && \
    update-alternatives --install /usr/bin/clang++ clang++ $(which clang++-15) 30

# OFED
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends -t jammy \
        dapl2-utils \
        ibutils \
        ibverbs-providers \
        ibverbs-utils \
        infiniband-diags \
        libdapl-dev \
        libdapl2 \
        libibmad-dev \
        libibmad5 \
        libibverbs-dev \
        libibverbs1 \
        librdmacm-dev \
        librdmacm1 \
        rdmacm-utils && \
    rm -rf /var/lib/apt/lists/*

# GDRCOPY version 2.2
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        make \
        wget && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://github.com/NVIDIA/gdrcopy/archive/v2.2.tar.gz && \
    mkdir -p /var/tmp && tar -x -f /var/tmp/v2.2.tar.gz -C /var/tmp -z && \
    cd /var/tmp/gdrcopy-2.2 && \
    mkdir -p /usr/local/gdrcopy/include /usr/local/gdrcopy/lib && \
    make prefix=/usr/local/gdrcopy lib lib_install && \
    rm -rf /var/tmp/gdrcopy-2.2 /var/tmp/v2.2.tar.gz
ENV CPATH=/usr/local/gdrcopy/include:$CPATH \
    LD_LIBRARY_PATH=/usr/local/gdrcopy/lib:$LD_LIBRARY_PATH \
    LIBRARY_PATH=/usr/local/gdrcopy/lib:$LIBRARY_PATH

# KNEM version 1.1.4
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates \
        git && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/tmp && cd /var/tmp && git clone --depth=1 --branch knem-1.1.4 https://gitlab.inria.fr/knem/knem.git knem && cd - && \
    mkdir -p /usr/local/knem && \
    cd /var/tmp/knem && \
    mkdir -p /usr/local/knem/include && \
    cp common/*.h /usr/local/knem/include && \
    rm -rf /var/tmp/knem
ENV CPATH=/usr/local/knem/include:$CPATH

# XPMEM branch master
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        autoconf \
        automake \
        ca-certificates \
        file \
        git \
        libtool \
        make && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/tmp && cd /var/tmp && git clone --depth=1 --branch master https://github.com/hjelmn/xpmem.git xpmem && cd - && \
    cd /var/tmp/xpmem && \
    autoreconf --install && \
    cd /var/tmp/xpmem &&   ./configure --prefix=/usr/local/xpmem --disable-kernel-module && \
    make -j$(nproc) && \
    make -j$(nproc) install && \
    rm -rf /var/tmp/xpmem
ENV CPATH=/usr/local/xpmem/include:$CPATH \
    LD_LIBRARY_PATH=/usr/local/xpmem/lib:$LD_LIBRARY_PATH \
    LIBRARY_PATH=/usr/local/xpmem/lib:$LIBRARY_PATH

# UCX https://github.com/openucx/ucx.git v1.14.1
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        autoconf \
        automake \
        binutils-dev \
        ca-certificates \
        file \
        git \
        libnuma-dev \
        libtool \
        make \
        wget && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/tmp && cd /var/tmp && git clone --depth=1 --branch v1.14.1 https://github.com/openucx/ucx.git ucx && cd - && \
    cd /var/tmp/ucx && \
    ./autogen.sh && \
    cd /var/tmp/ucx &&   ./configure --prefix=/usr/local/ucx --disable-assertions --disable-debug --disable-doxygen-doc --disable-logging --disable-params-check --enable-optimizations --without-cuda && \
    make -j$(nproc) && \
    make -j$(nproc) install && \
    rm -rf /var/tmp/ucx
ENV CPATH=/usr/local/ucx/include:$CPATH \
    LD_LIBRARY_PATH=/usr/local/ucx/lib:$LD_LIBRARY_PATH \
    LIBRARY_PATH=/usr/local/ucx/lib:$LIBRARY_PATH \
    PATH=/usr/local/ucx/bin:$PATH

# OpenMPI version 4.0.5
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bzip2 \
        file \
        hwloc \
        libnuma-dev \
        make \
        openssh-client \
        perl \
        tar \
        wget && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/tmp && wget -q -nc --no-check-certificate -P /var/tmp https://www.open-mpi.org/software/ompi/v4.0/downloads/openmpi-4.0.5.tar.bz2 && \
    mkdir -p /var/tmp && tar -x -f /var/tmp/openmpi-4.0.5.tar.bz2 -C /var/tmp -j && \
    cd /var/tmp/openmpi-4.0.5 &&  CC=clang CXX=clang++ ./configure --prefix=/usr/local/openmpi --disable-getpwuid --enable-orterun-prefix-by-default --with-ucx --without-cuda --without-verbs && \
    make -j$(nproc) && \
    make -j$(nproc) install && \
    rm -rf /var/tmp/openmpi-4.0.5 /var/tmp/openmpi-4.0.5.tar.bz2
ENV LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH \
    PATH=/usr/local/openmpi/bin:$PATH

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        libomp-dev \
        make \
        tar \
        wget && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/ECP-ExaGraph/miniVite/archive/refs/tags/v1.2.tar.gz; tar -xzvf v1.2.tar.gz; mv miniVite-1.2/ minivite

COPY Makefile /minivite


