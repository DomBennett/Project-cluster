#! /bin/usr/env python
# D.J. Bennett
'''
Read .sam file and convert to .fasta
'''

# LIBS
import os

# CONSTANTS
DATA_FILE = "P7810_1001.sorted.sam"
OUT_FILE = "P7810_1001.sorted.fasta"

# READ
DATA_FILE = os.path.join('data', DATA_FILE)
LINES = []
with open(DATA_FILE, "rU") as infile:
    for line in infile:
        LINES.append(line)

# CREATE EXTRACT EXON
DFLNS = []
SQS = []
for ln in LINES:
    spltln = ln.split('\t')
    sqid = spltln[0]
    coords = spltln[5]
    sq = spltln[9]
    coords = [e.split('S') for e in coords.split('M')]
    if len(coords[0]) == 2:
        strt = int(coords[0][0])
        end = strt + int(coords[0][1]) - 1
    else:
        strt = 0
        end = int(coords[0][0]) - 1
    SQS.append(sq[strt:end])
    DFLNS.append('> {0}'.format(sqid))

# WRITE OUT
OUT_FILE = os.path.join('data', OUT_FILE)
with open(OUT_FILE, "w") as outfile:
    for dfln, sq in zip(DFLNS, SQS):
        outfile.write(dfln)
        outfile.write('\n{0}\n\n'.format(sq))
