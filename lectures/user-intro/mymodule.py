#!/usr/bin/env python

"""An example of a module"""

def my_name(caller):

    """A function within a module"""

    print("My name is: ", __name__, "called from ", caller)


if __name__ == "__main__":

    my_name("a script")
