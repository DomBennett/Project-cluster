#! /bin/usr/env python
# D.J. Bennett
'''
Tabulate results from cdhits
'''

def tabulate(outfile, counts, fldrs):
    '''
    Convert cdhits results into .csv
    '''
    with open(outfile, "w") as outfile:
        outfile.write('folder,count\n')
        for fldr, count in zip(fldrs, counts):
            outfile.write('{0},{1}\n'.format(fldr, count))
