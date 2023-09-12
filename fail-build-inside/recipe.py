#!/usr/bin/env python

import hpccm

#Ubuntu 22.04 base image
Stage0 += baseimage(image='ubuntu:22.04')
Stage0 += gnu()

#Clang version 15...
compiler = llvm(version="15")
Stage0 += compiler

#Default version value is 4.0.5. OpenMPI supports 
Stage0 += ofed()
Stage0 += gdrcopy()
Stage0 += knem()
Stage0 += xpmem()
Stage0 += ucx(cuda=False, repository='https://github.com/openucx/ucx.git', branch="v1.14.1")
Stage0 += openmpi(cuda=False, infiniband=False, toolchain=compiler.toolchain, ucx=True)

Stage0 += apt_get(ospackages=['make', 'wget', 'tar', 'libomp-dev'])
Stage0 += shell(commands=['wget https://github.com/ECP-ExaGraph/miniVite/archive/refs/tags/v1.2.tar.gz; tar -xzvf v1.2.tar.gz; mv miniVite-1.2/ minivite'])
Stage0 += copy(src="Makefile", dest="/minivite")
#Stage0 += shell(commands=['cd minivite', 'make'])
