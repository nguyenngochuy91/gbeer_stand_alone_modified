#!/usr/bin/env python

import numpy as np
from Bio import Phylo
from PIL import Image
from os.path import expanduser
import os
import ntpath
import pickle
from ete2 import Tree, TreeStyle, NodeStyle

def scaleUpPhyloTree(inTreeFile,outTreeFile,scaleFactor):
    tree = Tree(inTreeFile)
    #tree = inTree
    #print type(tree)
    #print inTree.depths()
    #for key,value in inTree.depths().iteritems():
        #print key.total_branch_length
    for n in tree.traverse():
        dist = n._get_dist()
        #name = n.name
        #if (name.contains("_")):
            #names = name.
        #print dist
        n._set_dist(dist*scaleFactor)
    tree.write(outfile=outTreeFile)   
    #clade = inTree.get_terminals()
    #print clade
        #print type(key)
    #for node in inTree.traverse("postorder"):
        # Do some analysis on node
       #print node.name

def main():
    scaleUpPhyloTree("/home/jain/Downloads/ProOpDB/test_run_BSub2/tree/out_tree.nwk", "~/Downloads/ProOpDB/test_run_BSub2/tree/out_tree_updated.nwk", 10)


if __name__ == "__main__":
    main()