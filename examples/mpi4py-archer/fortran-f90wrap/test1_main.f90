program test1_main

  use test1
  implicit none

  integer :: ifail

  call MPI_Init(ifail)

  call mpi_fortran_operation(MPI_COMM_WORLD)

  call MPI_Finalize(ifail)

end program test1_main
