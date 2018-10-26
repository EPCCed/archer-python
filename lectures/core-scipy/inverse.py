# find inverse of matrix

import numpy as np
from scipy import linalg

a = np.array([[1,3,5], [2,5,1], [2,3,8]])

ainv = linalg.inv(a)

# check inverse gives identity 
identity = a.dot(ainv)

# This really is the identity if we take 1 sig. fig.
print(np.abs(np.around(identity, 0)))
