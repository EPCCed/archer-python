
#include <stdio.h>
#include <mpi.h>

int mpi_c_operation(MPI_Comm comm) {

  int rank;
  int size;
  int sum;

  MPI_Comm_rank(comm, &rank);
  MPI_Comm_size(comm, &size);

  printf("Hello from C rank %d of %d\n", rank, size);

  sum = 0;
  MPI_Reduce(&rank, &sum, 1, MPI_INT, MPI_SUM, 0, comm);

  if (rank != 0) return 0;

  printf("Root reports sum of ranks: %d (%d)\n", sum, ((size-1)*size)/2);

  return 0;
}
