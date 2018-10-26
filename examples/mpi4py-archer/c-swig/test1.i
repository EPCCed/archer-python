%module test1

%{

#include <mpi.h>
#include "test1.h"

%}

%include mpi4py/mpi4py.i
%mpi4py_typemap(Comm, MPI_Comm);

int mpi_c_operation(MPI_Comm comm);
