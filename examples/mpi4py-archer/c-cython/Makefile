#
#  Cython wrapper for mpi4py to C
#
#  Requires, on the front end (see note below):
#    module swap PrgEnv-cray PrgEnv-gnu
#    module swap gcc gcc/4.9.3
#    module load python-compute
#    make
#
# Typically, one might want, at the command line:
#   bash$ cython ...
#
# Unfortunately, python-compute has no command line cython, so
# we have to fake the generation of the wrapper.c code from
# wrapper.pyx source.
#
# Note this will barf with an ugly message at the compile stage,
# but it gets as far as we need. Just run "make" again to finish.
#
# IMPORTANT: The compiler used must be the same as that used to
# compile mpi4py. If, at run time, you see the error 
#
# "Attempting to use an MPI routine before initializing MPICH"
#
# it suggests a mismatch. Use ldd to check exactly which version
# is involved in mpi4py .so file and the wrapper.so file
#
# At the time of writing it's gnu/4.9.3 (see module stuff above).


CC = cc
CFLAGS = -fPIC
TEST = test1
PYTHON = python

INCLUDE_PYTHON = ${shell ${PYTHON} -c 'import sysconfig; print(sysconfig.get_path("include"))'}
INCLUDE_MPI4PY = ${shell ${PYTHON} -c 'import mpi4py; print( mpi4py.get_include())'}

# Generate the shared object
wrapper.so:	${TEST}.o wrapper.o
	$(CC) -shared -o wrapper.so $^

# Here's the fake "cython"
wrapper.c:	wrapper.pyx
	${PYTHON} setup.py build_ext --inplace

# Compile the C wrapper
wrapper.o:	wrapper.c
	${CC} -c -fPIC -I${INCLUDE_PYTHON} -I${INCLUDE_MPI4PY} $<

# Compile the C source
${TEST}.o:	${TEST}.c
	$(CC) -c $(CFLAGS) $<

clean:
	${RM} -rf *.o *.so wrapper.c build
