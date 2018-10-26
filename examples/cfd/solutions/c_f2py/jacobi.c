/* 
 * Jacobi iteration
 */
void jacobi(int m, int n, int niter, double *psi)
{

    // Local variables
    int i, j, iter;
    int idx, jdx, im1, ip1;
    double tmp[(m+2)*(n+2)];
    
    // Zero the tmp array
    for ( i=0; i<n+2; i++)  {
        for ( j=0; j<m+2; j++)  {
            // Compute correct index
            jdx  = i*(n+2) + j;
            tmp[jdx] = 0.0;
        }
    }
    // Jacobi iterations
    for (iter=0; iter<niter; iter++) {
        for ( i=1; i<n+1; i++)  {
            for ( j=1; j<m+1; j++)  {
                // Compute correct indices
                im1 = (i-1)*(n+2) + j;
                ip1 = (i+1)*(n+2) + j;
                jdx = i*(n+2) + j;
                tmp[jdx] = 0.25 * (psi[jdx-1]+psi[jdx+1]+psi[im1]+psi[ip1]);
            }
        }
        // Copy inner part of tmp to psi
        for ( i=1; i<n+1; i++)  {
            for ( j=1; j<m+1; j++)  {
                // Compute correct index
                jdx = i*(n+2) + j;
                psi[jdx] = tmp[jdx];
            }
        }
    }
}

