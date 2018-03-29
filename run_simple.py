import os
from stages.extract import compare_seq

wd = '/home/dom/Coding/Project-cluster/rpb2_test'


fldrs = [e for e in os.listdir(wd) if\
             os.path.isdir(os.path.join(wd, e))]
for fldr in fldrs:
    fldr = os.path.join(wd, fldr)
    print 'Working on [{0}] ...'.format(fldr)
    outfile = os.path.join(wd, fldr, 'refseq.fasta')
    compare_seq(fldr, outfile=outfile)
