#
#  SWIG wrapper for mpi4py to C
#
#  Requires, on the front end (see note below):
#    module swap PrgEnv-cray PrgEnv-gnu
#    module swap gcc gcc/4.9.3
#    module load python-compute
#    module load swig
#    make
#
#  IMPORTANT: The compiler used must be the same as that used to
#  compile mpi4py. If, at run time, you see the error 
#
#  "Attempting to use an MPI routine before initializing MPICH"
#
#  it suggests a mismatch. Use ldd to check exactly which version
#  is involved in mpi4py .so file and the _test1.so file
#
#  At the time of writing it's gcc/4.9.3 (see module stuff above).
#
#  Kevin Stratford kevin@epcc.ed.ac.uk


CC = cc
CFLAGS = -fPIC
SWIG = swig -python
PYTHON = python
TEST = test1

INCLUDE_PYTHON = \
	${shell ${PYTHON} -c 'import sysconfig; print( sysconfig.get_path("include"))'}
INCLUDE_MPI4PY = \
	${shell ${PYTHON} -c 'import mpi4py; print( mpi4py.get_include())'}


# Generate shared object. Note the prepended underscore _${NAME}.so
module:	${TEST}.o ${TEST}_wrap.o
	${CC} -shared -o _${TEST}.so $^


# Produce C wrapper source from the interface
${TEST}_wrap.c:	${TEST}.i ${TEST}.h
	${SWIG} -I${INCLUDE_MPI4PY} $<

# Compile C source
${TEST}.o:	${TEST}.c
	${CC} -c ${CFLAGS} $<

# Compile C wrapper
${TEST}_wrap.o:	${TEST}_wrap.c
	$(CC) -c -I${INCLUDE_PYTHON} -I${INCLUDE_MPI4PY} ${CFLAGS} $<

clean:
	${RM} -rf *o *pyc ${TEST}_wrap.c ${TEST}.py
