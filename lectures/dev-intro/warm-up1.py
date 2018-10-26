
""" A function to calculate the median of a list"""

def my_median(years):
    ages = []
    for y in years:
        ages.append(y - 1900)

    ages.sort()
    mid = len(ages)/2

    return ages[mid-1:mid+2]

years = [1989, 1955, 2011, 1943, 1975]
print(my_median(years))

# !! In Python 2.x, division operator '/' does integer
# division e.g.
#
# 3/2 = 1
#
# In Python 3.x, the '/' does real division
#
# 3/2 = 1.5
#
# For integer division in Python 3.x, use operator '//', 
# e.g.
#
# mid = len(ages)//2

