subroutine fibonacci(n, a_out)
  implicit none
  integer, intent(in) :: n
  real*8, dimension(n) :: a_out

  integer :: i

  do i = 1, n
    if (i.eq.1) then
      a_out(i) = 1.0
    elseif (i.eq.2) then
      a_out(i) = 1.0
    else
      a_out(i) = a_out(i-1) + a_out(i-2)
    end if
  end do

  return

end subroutine fibonacci
