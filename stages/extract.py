#! /bin/usr/env python
# J.S. Eriksson
# 2018-03-27
'''
Get sequence IDs from clusters from cdhit
'''

# LIBS
from stages.count import count
from stages.sequence import gt_sq
from tools.extract_tools import slct_exn
import os

# FUNCTIONS

def nmbr_cps(fldr):
     #todo pass dir/infile
    cps = {}
    dir_contents = os.listdir(fldr)
    clstr_fls = [e for e in dir_contents if e.endswith('.cl.clstr')]
    for clfl in clstr_fls:
        cps[clfl] = count(os.path.join(fldr, clfl))
    return cps


def rf_nms(cps_max, min_nsqs=10):
    '''
    From the exon with highest number of clusters, list all sequences from clusters with a minimum of 10 sequences.
    '''
    lines = []
    with open(cps_max, "rU") as infile:
        for line in infile:
            lines.append(line)
    nsqs = 0
    cls_sqs = []
    crrnt_sqs = []
    for line in lines:
        if line.find('>') == 0:
            if nsqs >= min_nsqs:
                cls_sqs.append(crrnt_sqs)
            nsqs = 0
            crrnt_sqs = []
        else:
            nsqs += 1
            crrnt_sqs.append(line)
    return cls_sqs

def extract(cls_sqs):
    '''
    Extract the name of read representing each cluster.
    '''
    refs_list = []
    for cl_sqs in cls_sqs:
        for c_sqs in cl_sqs:
            if c_sqs.endswith('*\n'):
                ref_list = c_sqs.split()[3]
                ref_list = ref_list.replace('...','')
                refs_list.append(ref_list)
    return refs_list


def compare_seq(fldr, outfile='test.fasta'):
    '''
    Return a list of sequences for Geneious.
    '''
    cps = nmbr_cps(fldr)
    cps_max = slct_exn(cps)
    cls_sqs = rf_nms(os.path.join(fldr, cps_max))
    refs_l = extract(cls_sqs)
    seq_fasta = gt_sq(cps, fldr)
    reference = []
    for r in refs_l:
        for k,v in seq_fasta.items():
            if k in r:
                reference.append('> {0}\n{1}\n'.format(k,v))
    with open(outfile, "w") as otfile:
        for i in reference:
            otfile.write(i)
