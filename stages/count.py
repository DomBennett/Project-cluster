#! /bin/usr/env python
# D.J. Bennett
'''
Count clusters from cdhit
'''

def count(clfl, min_nsqs=10):
    '''
    Count number of clusters
    '''
    lines = []
    with open(clfl, "rU") as infile:
        for line in infile:
            lines.append(line)
    nsqs = 0
    ncls = 0
    for line in lines:
        if line.find('>') == 0:
            if nsqs >= min_nsqs:
                ncls += 1
            nsqs = 0
        else:
            nsqs += 1
    return ncls
