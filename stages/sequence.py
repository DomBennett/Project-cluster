#! /bin/usr/env python
# J.S. Eriksson
# 2018-03-27


# LIBS
import os
from tools.extract_tools import slct_exn

# FUNCTIONS

def gt_sq(cps, fldr):
    '''
    Convert .fasta file into dictionary
    '''
    #dct_fst = {}
    sq_nms = []
    sqs = []
    OFL = slct_exn(cps) # replace .clstr to .fasta
    OFL = os.path.join(fldr, OFL)
    IFL = OFL.replace('.cl.clstr', '.fasta')
    with open(IFL, "rU") as infile:
        for line in infile:
            if line.startswith('>'):
                sq_nm = line.replace('>', '')
                sq_nm = sq_nm.strip()
                sq_nm = sq_nm.replace(' ', '_')    #If needed)
                sq_nms.append(sq_nm)
                #print sq_nms
            elif line.startswith('A') or line.startswith('C') or line.startswith('G') or line.startswith('T'):
                sqs.append(line.strip())
                #print sqs
    dct_fst = dict(zip(sq_nms, sqs))
    return dct_fst
