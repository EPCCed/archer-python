import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def x1_t(t,x1,x2,k,m):
    """Exact solution for mass 1 at time t based on positions
    x1, x2, and spring constant k. Assumes initial velocity
    is zero"""

    w = np.sqrt(k/m)
    a1 = (x1 + x2)/2.0
    a2 = (x1 - x2)/2.0
    return a1*np.cos(w*t) + a2*np.cos(np.sqrt(3)*w*t)


def x2_t(t,x1,x2,k,m):
    """Exact solution for mass 2 at time t based on positions
    x1, x2, and spring constant k. Assumes initial velocity
    is zero"""

    w = np.sqrt(k/m)
    a1 = (x1 + x2)/2.0
    a2 = (x1 - x2)/2.0
    return a1*np.cos(w*t) - a2*np.cos(np.sqrt(3)*w*t)

def vectorfield(w, t, p):
    """Defines the differential equations for the coupled 
    spring-mass system. Arguments:
        w :  vector of the state variables: w = [x1,v1,x2,v2]
        t :  time
        p :  vector of the parameters: p = [m,k] 
    """
    x1, v1, x2, v2 = w
    m, k = p

    # Create f = (x1',y1',x2',y2'):
    f = [v1, (-k * x1 + k * (x2 - x1)) / m, v2, (-k * x2 - k * (x2 - x1)) / m]

    return f

def plot_result(stoptime, x01, x02, k, m):

    # "vectorize" solutions to act on an array of times 
    x1_sol = np.vectorize(x1_t)
    x2_sol = np.vectorize(x2_t)

    t, x1, v1, x2, v2 = np.loadtxt('coupled_masses.dat', unpack=True)
    plt.figure(1, figsize=(10, 3.5))
    plt.xlabel('t') 
    plt.ylabel('x')
    plt.grid(True)
    plt.hold(True)

    # plot exact solutions
    time = np.linspace(0,stoptime,500)

    plt.plot(time, x1_sol(time,x01,x02,k,m), 'b-', linewidth=1)
    plt.plot(time, x2_sol(time,x01,x02,k,m), 'g-', linewidth=1)

    # plot numerical solutions
    plt.plot(t, x1, 'r*')
    plt.plot(t, x2, 'mo')

    plt.legend(('$x_{1,exact}$', '$x_{2,exact}$', '$x_{1,num}$', 
                '$x_{2,num}$'))
    plt.title('Mass Displacements for the\nCoupled Spring-Mass System')
    plt.show()

def main():

    # Parameters and initial values
    # Mass and spring constant
    m = 1.0
    k = 1.0
    # Initial displacements
    x01 = 0.5
    x02 = 0.0
    # Initial velocities (remember exact solution relies on
    # v01 = v02 = 0)
    v01 = 0.0
    v02 = 0.0

    # ODE solver parameters
    abserr = 1.0e-8
    relerr = 1.0e-6
    stoptime = 10.0
    numpoints = 50

    # Create time samples for the output of the ODE solver
    t = np.linspace(0, stoptime, numpoints)

    # Pack up the parameters and initial conditions as lists/arrays:
    p =  [m, k]
    w0 = [x01, v01, x02, v02]

    # Call the ODE solver

    wsol = odeint(vectorfield, w0, t, args=(p,), atol=abserr, rtol=relerr)

    with open('coupled_masses.dat', 'w') as f: 
        for t1, w1 in zip(t, wsol):
            print(f, t1, w1[0], w1[1], w1[2], w1[3])

    plot_result(stoptime, x01, x02, k,  m)

    return 0


if __name__ == "__main__":
    main()
