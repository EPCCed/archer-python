#
# ctypes coupling for mpi4py to C
#
# Requires, on the front end
#   module swap PrgEnv-cray PrgEnv-gnu
#   module load python-compute
#   make
#
# IMPORTANT
# mpi4py v 2.0 is required.
# For the coupling to work, we need mpi4py 2.0 (not the 1.3.1 coming
# from python-compute). The version here is built under PrgEnv-gnu.

CC = cc
CFLAGS = -fPIC
TEST = test1

# Generate a shared object
module:	${TEST}.o
	${CC} -shared -o ${TEST}.so $<

# Compile the C source
${TEST}.o:	${TEST}.c
	${CC} -c ${CFLAGS} $<

clean:
	${RM} -rf *.o *.so