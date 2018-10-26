import sys

years = [1989, 1955, 2011, 1943, 1975]

# save years to file

outputfn = "years.txt"

with open(outputfn, 'w') as fn:
    # output total number of years
    fn.write("{0:2d}\n".format(len(years)))
               
    for i in range(len(years)):
        fn.write("{0:2d} {1:2d}\n".format(i, years[i]))

# Read the file into a new list

inputfn = "years.txt"

with open("years.txt", 'r') as fn:
    # Read the number of entries (as a string)
    # Do not need this, but for consistency's sake...
    nyear = int(fn.readline())

    # Read in the entries (gives list of input strings)
    doc = fn.readlines()

# Use list comprehension to: 
# 1 - strip left/right whitespace from each string in doc 
# 2 - split each string into 'tokens' so each string becomes a list 
# of 2 elements, [number,  year]
# 3 - cast 2nd element in token (i.e. the year) to integer

newyears = [int( (line.strip()).split()[1] ) for line in doc]

print(newyears)

