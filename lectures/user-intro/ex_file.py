#!/usr/bin/env python

"""Example routines to read and write from/to file using open/close"""

def read_file(file_name):

    """Read the number of data items, and the data from the specified file;
       return the list of data"""

    inputfile = open(file_name, "r")

    # Read the number of entries (as a string); store as integer

    line = inputfile.readline()
    nitems = int(line)

    # Read in the entries (strip off the new line character;
    # split the line into separate "words"; store data wanted as integer)

    data = []

    for _ in range(nitems):
        line = inputfile.readline()
        line = line.rstrip()
        tokens = line.split()
        data.append(int(tokens[1]))

    inputfile.close()

    return data


def write_file(file_name, data):

    """Write number of data items, and data items one per line"""

    outputfile = open(file_name, 'w')

    outputfile.write("{0:2d}\n".format(len(data)))

    for item, datum in enumerate(data):
        outputfile.write("{0:2d} {1:2d}\n".format(item, datum))

    outputfile.close()
