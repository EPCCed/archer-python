subroutine mpi_fortran_operation(comm)

  integer, intent(in) :: comm

  integer :: rank
  integer :: size
  integer :: ifail

  call MPI_Comm_rank(comm, rank, ifail)
  call MPI_Comm_size(comm, size, ifail)

  write (*,*) 'Fortran has rank ', rank, ' of ', size

  return

end subroutine mpi_fortran_operation
