# Requires invokation by python interpreter on back end.

import sys
import wrapper
from mpi4py import MPI

def main(argv):

    rank = MPI.COMM_WORLD.rank
    size = MPI.COMM_WORLD.size
    sys.stdout.write("Hello from rank {:2d} of {:2d}\n".format(rank, size))

    comm = MPI.COMM_WORLD
    wrapper.cython_mpi_c_operation(comm)

    return 0


# Execute

if __name__ == "__main__":
    main(sys.argv[1:])

