# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:12:45 2018

@author: ottoj
"""

import sys     # we need this library to deal with operating system

infilename = sys.argv[1]
outfilename = sys.argv[2]

""" Opens two files and copies one into the other line by line. """
infile = open(infilename)
outfile = open(outfilename,'w')
    
for line in infile:
    outfile.write(line)
        
infile.close()
outfile.close()