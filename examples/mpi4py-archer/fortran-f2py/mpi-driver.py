# Requires invokation by python interpreter on back end.

import sys

import mpi4py.MPI
import fortran

def main(argv):

    rank = mpi4py.MPI.COMM_WORLD.rank
    size = mpi4py.MPI.COMM_WORLD.size
    sys.stdout.write("Hello from rank {:2d} of {:2d}\n".format(rank, size))

    comm = mpi4py.MPI.COMM_WORLD.py2f()

    fortran.mpi_fortran_operation(comm)

    return 0


# Execute

if __name__ == "__main__":
    main(sys.argv[1:])

