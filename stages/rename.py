#! /bin/usr/env python
# J.S. Eriksson
# 2018-04-05
'''
Re-name reference reads to species name + copy number
'''

def rename_ref(infile2, outfile2, fl):
    new_refnms = []
    i = 0
    with open(infile2, "rU") as infile:        
        for line in infile:
            if line.startswith('>'):
                i += 1
                l = line.replace(line, '>{0}_copy_{1}'.format(fl, i))
                new_refnms.append(l)
            else:
                new_refnms.append(line)    
        #return new_refnms
    
    with open(outfile2, "w") as otfile2:
        for i in new_refnms:
            otfile2.write('{0}\n'.format(i))            