#
# Build shared library to allow C Jacobi function to be
# called from Python. Uses f2py and requires a C compiler
# to be installed.
#
# ---- Compile and Link --------------------------- 
jacobi.so: jacobi.c jacobi.pyf
	f2py -c jacobi.pyf jacobi.c
