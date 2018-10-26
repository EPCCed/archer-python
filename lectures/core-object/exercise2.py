"""An exercise in python class structure"""

class MyRNG(object):

    """A simple random number generator based on
       s -> (a*s + c) % m
    """

    A = 1389796
    C = 0
    M = 2147483647

    def __init__(self, state):

        """The state should be a +ve integer"""

        self.state = state

    def reap(self):

        """Advance and return the current state"""

        self.state = (MyRNG.A*self.state + MyRNG.C) % MyRNG.M
        return self.state

    def double(self):

        """Generate a floating point number on
        the interval [0.0, 1.0)"""

        return 1.0*self.reap() / MyRNG.M
