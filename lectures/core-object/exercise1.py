"""An exercise in python class structure"""

class MyComplex(object):

    """A very simple Complex number class
    with add and multiply instance methods"""

    def __init__(self, re, im):

        """Complex number with real and imaginary parts"""

        self.re = re
        self.im = im

    def add(self, c):

        """Add c to self"""

        self.re += c.re
        self.im += c.im

    def multiply_by(self, c):

        """Multiply self by c"""

        re = self.re*c.re - self.im*c.im
        im = self.re*c.im + self.im*c.re

        self.re = re
        self.im = im
