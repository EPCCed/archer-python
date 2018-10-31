#!/usr/bin/env python

def my_name(caller):

    print("My name is: ", __name__, "called from ", caller)
    
if __name__ == "__main__":

    my_name("a script")
