#! /bin/usr/env python
# D.J. Bennett
'''
Read .sam file, extract only the exon-length sections of sequence and write
out as .fasta
'''

# LIBS
from tools.convert_tools import extract_exon

# FUNCTION
def convert(infile, outfile):
    '''
    .sam to .fasta.
    '''
    lines = []
    with open(infile, "rU") as infile:
        for line in infile:
            lines.append(line)
    dflns_sqs = extract_exon(lines)
    with open(outfile, "w") as outfile:
        for dfln, seq in dflns_sqs:
            outfile.write(dfln)
            outfile.write('\n{0}\n\n'.format(seq))
