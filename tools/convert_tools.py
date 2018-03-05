#! /bin/usr/env python
# D.J. Bennett
'''
Convert tools
'''

def read_sam_file(infile):
    '''
    Read .sam, return list of lines.
    '''
    lines = []
    with open(infile, "rU") as infile:
        for line in infile:
            lines.append(line)
    return lines

def extract_exon(lines):
    '''
    Extract exon from .sam lines. Return zip(dfln, sq)
    '''
    dflns = []
    sqs = []
    for line in lines:
        spltln = line.split('\t')
        sqid = spltln[0]
        coords = spltln[5]
        seq = spltln[9]
        coords = [e.split('S') for e in coords.split('M')]
        if len(coords[0]) == 2:
            strt = int(coords[0][0])
            end = strt + int(coords[0][1]) - 1
        else:
            strt = 0
            end = int(coords[0][0]) - 1
        sqs.append(seq[strt:end])
        dflns.append('> {0}'.format(sqid))
    return zip(dflns, sqs)
