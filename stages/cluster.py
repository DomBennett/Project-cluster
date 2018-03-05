#! /bin/usr/env python
# D.J. Bennett
'''
Run cd-hits for .fasta.
'''

# LIBS
import sys
import os
import subprocess

# FUNCTION
def cluster(infile, cdhit, thrds=1):
    '''
    Run cd-hit
    '''
    outfile = infile.replace('.fasta', '.cl')
    cmd = '{0} -i {1} -o {2} -c 1.0 -T {3}'.format(cdhit, infile, outfile,\
                                                   thrds)
    # shell, security risk?
    log = 'cdhits_log'
    with open(log, 'w') as log:
        out = subprocess.call(cmd, shell=True, stdout=log, stderr=log)
    if out != 0:
        sys.exit('cdhits failed to run. See `cdhits_log`.\nCommand: [{0}]'.\
                  format(cmd))
    else:
        os.remove(log)
