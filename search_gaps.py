# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 21:24:15 2026

@author: mcing
The aim of this script is to read a fasta file, and search for the,
position of gaps in a fasta file. it then outputs them in into a bed file
"""

import re
import sys

def search_gaps(input_fasta):
    headers = ""
    sequences = {}
    output_file = "gaps.bed"
    
    with open(input_fasta, "r") as infile, open(output_file, "w") as outfile:
        outfile.write("header\tstart\tend\n") #this will create the column headings
        for line in infile:
            line = line.strip() #remove the white spaces
            if line.startswith(">"):
                headers = line
                sequences[headers] = ""  #empty dictionary, which only has >htloog
            else:
                sequences[headers] += line
        #We will use a regular expression inside this and find a
        #Then I will write those into an output file that might be a
        #dictionary or a text file
        for header, seq in sequences.items():
            for match in re.finditer(r"N+", seq):
                start = match.start() + 1
                end = match.end()
                outfile.write(f"{header}\t{start}\t{end}\n") #This will populate the
    
    return output_file

if __name__ == "__main__": #This ensures that it runs  in the command line terminal
    input_fasta = sys.argv[1]
    result = search_gaps(input_fasta)
    print(f"Results written to: {result}")                    
                
            