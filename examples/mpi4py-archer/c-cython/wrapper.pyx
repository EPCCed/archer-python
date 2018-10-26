
cimport mpi4py.MPI as MPI

cdef extern from "mpi.h":
     ctypedef int MPI_Comm

cdef extern from "test1.h":
     int mpi_c_operation(MPI_Comm comm)

def cython_mpi_c_operation(MPI.Comm comm not None ):
    cdef MPI_Comm c_comm = comm.ob_mpi
    mpi_c_operation(c_comm)
