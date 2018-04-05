import os
from stages.extract import compare_seq
from stages.rename import rename_ref

wd = './data'


fldrs = [e for e in os.listdir(wd) if\
             os.path.isdir(os.path.join(wd, e))]
for fldr in fldrs:
    fldr = os.path.join(wd, fldr)
    print 'Working on [{0}] ...'.format(fldr)
    outfile1 = os.path.join(wd, fldr, 'refseq_original.fasta')
    compare_seq(fldr, outfile=outfile1)
    
for fl in fldrs:
    print "working with folder {0}".format(fl)
    infile2 = os.path.join(wd, fl, 'refseq_original.fasta')
    outfile2 = os.path.join(wd, fl, '{0}_refseq.fasta'.format(fl))
    rename_ref(infile2, outfile2, fl)    