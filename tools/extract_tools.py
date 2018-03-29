#! /bin/usr/env python
# J.S. Eriksson
# 2018-03-27
'''
Extraction tools
'''

# LIBS
import operator


def slct_exn(cps):
    '''
    Select the exon with most copies, return file name
    '''
    cps_max= max(cps.items(), key=operator.itemgetter(1))[0]
    #print cps_max
    return cps_max