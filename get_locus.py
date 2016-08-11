#!/usr/bin/env python
"""
Created on Wed Jul 27 16:14:25 2016
@author: huyn
@purpose: getting the old_locus tag
"""
from Bio import SeqIO
import os
import time

protein_dir ="../protein/"
name = "gene_block_names_and_genes.txt"
###############################################################################
## Helper function to parse arguments, check directoring, ...
###############################################################################
# traverse and get the file
def traverseAll(path):
    res=[]
    for root,dirs,files in os.walk(path):
        for f in files:
            res.append(root+f)
    return res

# get the LOCUS from locus file
locus =[]
infile = open("locus","r")
modify = infile.read().split('\n')[0]
for item in modify.split('\t')[1:]:
    locus.append(item)

#walking through the protein dir to get the locus tag from the LOCUS file name
locus_tag =[]
dic={}
res = traverseAll(protein_dir)
for r in res:
    if r[11:21] in locus:
        # read this genbank file
        record = SeqIO.read(r,"gb")
        for feature in record.features:
            if feature.type =='CDS':
                locus_tag.append(feature.qualifiers['old_locus_tag'][0])
                dic[r[11:21]]= feature.qualifiers['old_locus_tag'][0]
# print locus_tag
outfile = open(name,'w')
outfile.write('operon')
for item in locus_tag:
    outfile.write('\t'+item)
outfile.write('\n')
outfile.close()                
# write the map for protein id and locus tag
outfile = open("protein_locus",'w')
for key in dic:
    outfile.write(key+','+dic[key]+'\t')
outfile.write('\n')
outfile.close()  
