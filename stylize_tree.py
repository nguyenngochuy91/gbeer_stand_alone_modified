#!/usr/bin/env python
import sys
sys.path = ['','/home/idoerg/soft/ete'] + sys.path[1:]
from ete3 import Tree, TreeStyle, TextFace, NodeStyle
def draw_tree(inpath):
    tb = Tree(inpath)
    ts=TreeStyle()
    ns = NodeStyle()
    ns["vt_line_width"] = 4
    ns["hz_line_width"] = 4
    ns["vt_line_type"] = 0
    ns["hz_line_type"] = 0
    tb.set_style(ns)
    for node in tb.traverse():
        node.img_style = ns
    for leaf in tb.get_leaves():
        if "Yucatan_Mexico" in leaf.name:
#        if "Mexico" in leaf.name and "Yuc-" in leaf.name:
            leaf.add_face(TextFace(leaf.name, bold=True, fsize=28),column=0,
                          position="branch-right")
            print(dir(leaf))
        else:
            leaf.add_face(TextFace(leaf.name,fstyle="normal",fsize=28),column=0,
            position="branch-right")
    ts.show_leaf_name = False
    ts.optimal_scale_level = "mid"
    #ts.branch_vertical_margin = 10 # 10 pixels between adjacent branches
    ts.scale =  10000 # Branch length
    #ts.force_topology = True
    ts.complete_branch_lines_when_necessary = True
    ts.show_scale = False
#    ts.show_branch_length=True
    ts.extra_branch_line_type = 0
    tb.render(inpath+".png", dpi=600, w=10,units="in", tree_style=ts)
    tb.show(tree_style=ts)

if __name__ == '__main__':
    draw_tree(sys.argv[1])
