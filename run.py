#! /bin/usr/env python
# D.J. Bennett
'''
Identify clusters from .sam using cd-hit
'''

# LIBS
import sys
import os
from stages.convert import convert

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit('Run as: `python run.py [WORKING DIRECTORY]`')
    WRKDR = str(sys.argv[1])
    SAM_FLS = [e for e in os.listdir(WRKDR) if e.find('.sam') != -1]
    if len(SAM_FLS) > 1:
        raise IOError('Too many .sam files in WD')
    if len(SAM_FLS) == 0:
        raise IOError('No .sam files in WD')
    INFILE = SAM_FLS[0]
    OUTFILE = INFILE.replace('.sam', '.fasta')
    INFILE = os.path.join(WRKDR, INFILE)
    OUTFILE = os.path.join(WRKDR, OUTFILE)
    print 'Converting ...'
    convert(infile=INFILE, outfile=OUTFILE)
    print 'Running cd-hits ...'
    print 'Creating tabular output ...'
