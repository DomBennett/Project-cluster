#! /bin/usr/env python
# D.J. Bennett
'''
Identify and count clusters from .sam file using cdhit.
Generates a .csv for number of clusters for a series of .sam files.
.sam files must be contained in separate folders in wd.
See run.py --help for usage.
'''

# LIBS
from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import argparse
from datetime import datetime
from stages.convert import convert
from stages.cluster import cluster
from stages.count import count
from stages.tabulate import tabulate

def parse_args():
    """Read arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-wd", help="Working directory containing .sam",\
                        required=True, type=str)
    parser.add_argument("-ot", help="Outfile .csv", required=True, type=str)
    parser.add_argument("-cdhit", help="Syspath to cdhit",\
                        default='cdhit', type=str)
    parser.add_argument("-minnsqs",\
                        help="Minimum number of sequences in a cluster",\
                        default=10, type=int)
    parser.add_argument("-threads", help="Number of threads", default=1,\
                        type=int)
    return parser.parse_args()

if __name__ == "__main__":
    print('Started [{0}]'.format(datetime.today().\
                          strftime("%A, %d %B %Y %I:%M%p")))
    ARGS = parse_args()
    FLDRS = [e for e in os.listdir(ARGS.wd) if\
             os.path.isdir(os.path.join(ARGS.wd, e))]
    if not FLDRS:
        sys.exit('-wd must be a parent folder containing a list of folders')
    CNTS = []
    for fldr in FLDRS:
        fldr = os.path.join(ARGS.wd, fldr)
        print('Working on [{0}] ...'.format(fldr))
        SAM_FLS = [e for e in os.listdir(fldr) if e.find('.sam') != -1]
        if len(SAM_FLS) > 1:
            sys.exit('Too many .sam files in [{0}]'.format(fldr))
        if len(SAM_FLS) == 0:
            sys.exit('No .sam files in [{0}]'.format(fldr))
        INFILE = SAM_FLS[0]
        OUTFILE = INFILE.replace('.sam', '.fasta')
        INFILE = os.path.join(fldr, INFILE)
        OUTFILE = os.path.join(fldr, OUTFILE)
        print('... converting')
        convert(infile=INFILE, outfile=OUTFILE)
        print('... running cd-hits')
        CLFILE = cluster(infile=OUTFILE, cdhit=ARGS.cdhit, thrds=ARGS.threads)
        print('... counting clusters')
        CNTS.append(count(clfl=CLFILE, min_nsqs=ARGS.minnsqs))
        print('Done.')
    tabulate(outfile=ARGS.ot, counts=CNTS, fldrs=FLDRS)
    print('Completed [{0}]'.format(datetime.today().\
                            strftime("%A, %d %B %Y %I:%M%p")))
