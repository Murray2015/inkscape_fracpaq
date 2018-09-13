# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 10:27:57 2018

@author: murray hogget - murrayhoggett@gmail.com 
"""

########## Change these variables below this line ##########
infile = "fake_fauls.svg" # Note, needs the full filename including .svg extension. 
outfilename = "fake_fauls_12092018" # note, does not need .txt extension. 
########## Change the variables above this line   ##########



def simple_lines_3(infile, outfilename):
    '''
    Takes a single svg, written by inkscape, and outputs
    a textfile of the absolute paths for nodes, in a tab 
    delimited format. Splits lines by colour, found by
    searching the textstring in the attributes, and thus 
    should handle different layers and different colours within
    the same layer, as long as different fractures sets are coloured
    differently. Requires absolute paths to be set in
    inkscape (Edit > Preferences > SVG > paths > Absolute). 
    Use pentool in inkscape with single clicks to 
    make straight paths. Does not handel benzier curves.
    outputs:
    infile_master.txt - file of all fractures 
    infile_XXXXXX_converted.txt - file of all fractures of a single colour. 
    As many files as there are different colours will be generated.'''
    from xml.dom import minidom
    import re
    # Get xml from .svg
    doc = minidom.parse(infile)  
    path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
    style_strings = [path.getAttribute('style') for path in doc.getElementsByTagName('path')]
    doc.unlink()
    # Open file connection for master file. 
    master_file = open(outfilename + "_master.txt", "w")
    counter=1
    colours = dict()
    print("Printing fracture coordinates both to python terminal and to outfilename...")
    for j in range(len(path_strings)):
        raw_line = path_strings[j]
        raw_style = style_strings[j]
        # Get stroke colour string
        stroke = re.search('stroke:#(.+?);', raw_style).group(1)
        # Format path into FracPaQ format 
        processed_line = raw_line.replace("M", "").lstrip().replace(" ", "\t").replace(",", "\t")
        print(processed_line)
        # Check if colour is in dict. If yes, write to already open file. If not, open file
        # for that colour then write processed string into it. 
        if stroke in colours.keys():
            colours[stroke].write(processed_line + "\n")
        else:
            filename = outfilename + "_" + stroke + "_converted.txt"
            colours[stroke] = open(filename, "w")
            colours[stroke].write(processed_line + "\n")
        master_file.write(processed_line + "\n")
        print("\nNew path, path number {}\n".format(counter))
        counter +=1
    # Close all file connections
    master_file.close()
    for k in colours.keys():
        colours[k].close()
    print("Finished processing files! Files should be in the directory this script is in.")


simple_lines_3(infile=infile, outfilename=outfilename)

