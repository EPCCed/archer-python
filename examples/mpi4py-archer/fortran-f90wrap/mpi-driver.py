# Requires invokation by python interpreter on back end.

import sys

from mpi4py import MPI
import fortran

def main(argv):

    rank = MPI.COMM_WORLD.rank
    size = MPI.COMM_WORLD.size
    sys.stdout.write("Hello python rank {:2d} of {:2d}\n".format(rank, size))

    # Get the communicator handle
    comm = MPI.COMM_WORLD.py2f()

    fortran.test1.mpi_fortran_operation(comm)

    return 0


# Execute

if __name__ == "__main__":
    main(sys.argv[1:])

