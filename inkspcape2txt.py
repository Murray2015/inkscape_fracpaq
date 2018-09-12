# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 09:06:04 2018

@author: murray
"""

import sys 
argv_infile = sys.argv[1]
argv_outfilename = sys.argv[2]

def simple_lines(infile, outfilename):
    '''
    Takes a single svg, written by inkscape, and outputs
    a textfile of the absolute paths for nodes, in a tab 
    delimited format. Requires absolute paths to be set in
    inkscape. Does not handel curves. Does not handle layers.
    Does not handle colours.'''
    from svgpathtools import svg2paths
    paths, attributes = svg2paths(infile)
    file = open(outfilename, "w")
    counter=1
    print("Print lines to terminal and to outfilename...")
    for j in attributes:
        raw_line = j['d']
        processed_line = raw_line.replace("M", "").lstrip().replace(" ", "\t").replace(" ", "\t").replace(",", "\t")
        print(processed_line)
        file.write(processed_line + "\n")
        print("\nNew path, number {}\n".format(counter))
        counter +=1
    file.close() 
    
simple_lines(infile=argv_infile, outfilename=argv_outfilename)









def simple_lines_2(infile, outfilename):
    '''
    Takes a single svg, written by inkscape, and outputs
    a textfile of the absolute paths for nodes, in a tab 
    delimited format. Requires absolute paths to be set in
    inkscape. Does not handel curves. Does not handle layers.
    Does not handle colours.'''
    from xml.dom import minidom
    doc = minidom.parse("fake_fauls.svg")  # parseString also exists
    path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
    doc.unlink()
    file = open(outfilename, "w")
    counter=1
    print("Print lines to terminal and to outfilename...")
    for j in path_strings:
        raw_line = j
        processed_line = raw_line.replace("M", "").lstrip().replace(" ", "\t").replace(" ", "\t").replace(",", "\t")
        print(processed_line)
        file.write(processed_line + "\n")
        print("\nNew path, number {}\n".format(counter))
        counter +=1
    file.close() 
    
simple_lines_2(infile=argv_infile, outfilename=argv_outfilename)

