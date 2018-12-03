#!/usr/bin/env python

"""Computes a median from a list of dates of birth"""

import datetime

def my_median(dobs, now):

    """Compute a median from a list of dates of birth in year now"""

    ages = []
    for year in dobs:
        ages.append(now - year)
    
    ages.sort()
    nages = len(ages)
    
    if (nages % 2 == 0):
        median = (ages[nages//2 - 1] + ages[nages//2])/2
    else:
        median = ages[nages//2]
        
    return median
    
if __name__ == "__main__":

    dates_of_birth = [1989, 1955, 2011, 1943, 1976]
    now = datetime.datetime.now()
    
    median = my_median(dates_of_birth, now.year)
    print(median)
