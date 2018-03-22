#! /bin/usr/env python
# D.J. Bennett
'''
Run cdhit for .fasta.
'''

# LIBS
import sys
import os
import subprocess

# FUNCTION
def cluster(infile, cdhit, lngthfrctn, thrds=1):
    '''
    Run cdhit
    '''
    outfile = infile.replace('.fasta', '.cl')
    cmd = '{0} -i {1} -o {2} -c 1.0 -l {3} -T {4} -d 0'.format(cdhit, infile, outfile,\
                                                        lngthfrctn, thrds)
    # shell, security risk?
    logfl = 'cdhit_log'
    with open(logfl, 'w') as log:
        out = subprocess.call(cmd, shell=True, stdout=log, stderr=log)
    if out != 0:
        sys.exit('cdhit failed to run. See `{0}` for details.\nCommand: [{1}]'.\
                  format(logfl, cmd))
    else:
        os.remove(logfl)
    return outfile
