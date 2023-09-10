#!/usr/bin/env python

import hpccm

#Ubuntu 22.04 base image
Stage0 += baseimage(image='ubuntu:22.04')
#Stage0 += gnu()

#Clang version 15...
compiler = llvm(version="15")
Stage0 += compiler

#Default version value is 4.0.5. OpenMPI supports 
Stage0 += openmpi(cuda=False, infiniband=False, toolchain=compiler.toolchain, ucx=True)

#g++-12 seems to be needed because of a clang-15 bug: https://stackoverflow.com/questions/26333823/clang-doesnt-see-basic-headers
Stage0 += apt_get(ospackages=['make', 'wget', 'tar', 'g++-12', 'libomp-dev'])
Stage0 += shell(commands=['wget https://github.com/ECP-ExaGraph/miniVite/archive/refs/tags/v1.2.tar.gz; tar -xzvf v1.2.tar.gz'])