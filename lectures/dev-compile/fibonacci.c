
int fibonacci(int n, double * a_out) {

  int i;

  for (i = 0; i < n; i++) {

    if (i == 0) {
      a_out[i] = 1.0;
    }
    else if (i == 1) {
      a_out[i] = 1.0;
    }
    else {
      a_out[i] = a_out[i-1] + a_out[i-2];
    }
  }

  return 0;
}
