# Docker container created with NVIDIA's HPCCM recipe.

# Building:

you can just: 

`hpccm --recipe ./recipe.py --format docker > Dockerfile`

to generate the Dockerfile and then:

`docker build -t hpccm-minivite`

to build the container. Or you can use the "build.sh" script in this repo.

# Using the minivite application:

You can:

`docker pull marcomontevechi/hpccm-minivite:1.0 && docker run --rm -it marcomontevechi/hpccm-minivite:1.0 sh -c "mpirun --allow-run-as-root -n 2 /minivite/miniVite -n 300"`

or just use the test.sh script in this repo.
