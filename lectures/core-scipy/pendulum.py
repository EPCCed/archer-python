# Plot the numerical and exact solutions for a simple pendulum

# to inline plots in a notebook, uncomment line below
# %matplotlib inline

import numpy as np

import matplotlib.pyplot as plt
plt.plot(t, solution[:, 0], 'ro', label='theta(t)')
plt.plot(tex[0:], pendulumTheta(tex[0:],theta0,b,m,g,length), 'r-', label='exact theta(t)')
plt.plot(t, solution[:, 1], 'bv', label='omega(t)')
plt.plot(tex[0:], pendulumOmega(tex[0:],theta0,b,m,g,length), 'b-', label='exact omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
