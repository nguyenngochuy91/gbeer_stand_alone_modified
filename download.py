#!/usr/bin/env python
''' Author  : Huy Nguyen
    Program : script to download all bactaria from ncbi
    Start   : 05/08/2016
    End     : 05/08/2016
'''
import os
import time
# download the assembly_sumary.txt
cmd = "wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt"
os.system(cmd)

# get swk the complete genome and latest verion
cmd = """
awk -F "\t" '$12=="Complete Genome" && $11=="latest"{print $20}' assembly_summary.txt > ftpdirpaths
"""
os.system(cmd)

# Append the filename of interest, in this case "*_genomic.gbff.gz" to the FTP 
# directory names. One way to do this would be using the following awk command
cmd = """
awk 'BEGIN{FS=OFS="/";filesuffix="genomic.gbff.gz"}{ftpdir=$0;asm=$10;file=asm"_"filesuffix;print ftpdir,file}' ftpdirpaths > ftpfilepaths
"""
os.system(cmd)

try:
    os.mkdir("genomes_all_bacteria")
except:
    print ("the directory genomes_all_bacteria has been made")
directory = "genomes_all_bacteria/"
infile = open("ftpfilepaths","r")
for file in infile.readlines():
    file = file.strip()
    name = file.split("/")[-1]
    cmd = "wget {} -P {}".format(file,directory)
    # download the file
    os.system(cmd)
    fileDownload = directory+name
    # gunzip the file, remove the download file
    cmd = "gunzip {}".format(fileDownload)
    os.system(cmd)

    