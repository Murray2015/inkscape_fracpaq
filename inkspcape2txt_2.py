# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 10:27:57 2018

@author: murray
"""

#import sys 
#argv_infile = sys.argv[1]
#argv_outfilename = sys.argv[2]

# Create tempvars instead of argv's
argv_infile = "fake_fauls.svg"
argv_outfilename = "fake_fauls_12092018.txt"

def simple_lines_2(infile, outfilename):
    '''
    Takes a single svg, written by inkscape, and outputs
    a textfile of the absolute paths for nodes, in a tab 
    delimited format. Requires absolute paths to be set in
    inkscape. Does not handel curves. Does not handle layers.
    Does not handle colours.'''
    from xml.dom import minidom
    doc = minidom.parse(argv_infile)  # parseString also exists
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




def simple_lines_3(infile, outfilename):
    '''
    Takes a single svg, written by inkscape, and outputs
    a textfile of the absolute paths for nodes, in a tab 
    delimited format. Splits linesets by colour, found by
    searching the textstring in the attributes, and thus 
    should handle different layers and different colours within
    the same layer, as long as different fractures sets are coloured
    differently. Requires absolute paths to be set in
    inkscape (Edit > Preferences > SVG > paths > Absolute). 
    Use pentool in inkscape with single clicks to 
    make straight paths. Does not handel benzier curves.'''
    from xml.dom import minidom
    import re
    doc = minidom.parse(argv_infile)  
    path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
    style_strings = [path.getAttribute('style') for path in doc.getElementsByTagName('path')]
    doc.unlink()
    counter=1
    colours = dict()
    print("Print lines to terminal and to outfilename...")
    for j in range(len(path_strings)):
        raw_line = path_strings[j]
        raw_style = style_strings[j]
        stroke = re.search('stroke:#(.+?);', raw_style).group(1)
        processed_line = raw_line.replace("M", "").lstrip().replace(" ", "\t").replace(" ", "\t").replace(",", "\t")
        print(processed_line)
        if stroke in colours.keys():
            colours[stroke].write(processed_line + "\n")
        else:
            filename = stroke + "_converted.txt"
            colours[stroke] = open(filename, "w")
            colours[stroke].write(processed_line + "\n")
        print("\nNew path, number {}\n".format(counter))
        counter +=1
    for k in colours.keys():
        colours[k].close()


simple_lines_3(infile=argv_infile, outfilename=argv_outfilename)

