#
#  Fortran from mpi4py via f90wrap
#
#  This requires f90wrap be installed. Briefly,
#
#  module swap PrgEnv-cray PrgEnv-gnu
#  module swap gcc gcc/4.9.3
#  module load python-compute
#  module load pc-numpy
#
#  and, e.g., from the current directory, to build f90wrap
#
#  git clone https://github.com/jameskermode/f90wrap.git
#  cd f90wrap
#  export PYTHONPATH=$PYTHONPATH:`pwd`/lib/python2.7/site-packages
#  export PATH=$PATH:`pwd`/bin
#  python setup.py install --prefix=`pwd`
#
#  Return to the current directory and
#  make
#
#
#  IMPORTANT: The C compiler used must be the same as that used to
#  compile mpi4py. If, at run time, you see the error 
#
#  "Attempting to use an MPI routine before initializing MPICH"
#
#  it suggests a mismatch. Use ldd to check exactly which version
#  is involved in mpi4py .so file and the _fortran.so file
#
#  At the time of writing it's gcc/4.9.3 (see module stuff above).


TEST=test1
EXT_MODULE_NAME=fortran

# Compile the extension module
_${EXT_MODULE_NAME}.so:	${TEST}.o f90wrap_${TEST}.f90
	f2py-f90wrap -c --f90exec=ftn -m _${EXT_MODULE_NAME} ${TEST}.o f90wrap_${TEST}.f90

# Generate the module.py and wrapped f90 files
f90wrap_${TEST}.f90: ${TEST}.f90
	f90wrap -m ${EXT_MODULE_NAME} ${TEST}.f90

# Compile the source
${TEST}.o:	${TEST}.f90
	ftn -c -fPIC $^


clean:
	rm -rf ${EXT_MODULE_NAME}.py _${EXT_MODULE_NAME}.so f90wrap_${TEST}.f90 ${TEST}.o ${TEST}.mod *.pyc
