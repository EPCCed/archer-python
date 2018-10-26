# Requires invocation by python interpreter on back end.

import sys

from mpi4py import MPI
import test1

def main(argv):

    rank = MPI.COMM_WORLD.rank
    size = MPI.COMM_WORLD.size
    sys.stdout.write("Hello python rank {:2d} of {:2d}\n".format(rank, size))

    comm = MPI.COMM_WORLD

    test1.mpi_c_operation(comm)

if __name__ == "__main__":
    main(sys.argv[1:])

