#!/usr/bin/env python3

# import argparse library
import argparse
import re

# create parser object
parser = argparse.ArgumentParser()

# create argument group
required = parser.add_argument_group('Required arguments')

# add argument to group
required.add_argument('-i', '--input', type=str, help='Path to input file', required=True)

# parse the arguments into variables
args = parser.parse_args()

# open file
file_in = open(args.input)

# read file contents
lines = file_in.readlines()
sequence = []
header = []
#just sequence
for line in lines:
        if not line.startswith('>'):
                sequence.append(line.removesuffix("\n"))
        else:
                header.append(line)
#length of sequence
def     length(seq):
        count = 1
        for i in seq:
                length = len(i)
                print("The length of sequence is:" + str(length))
                if re.search('^M', i):
                        print("Sequence starts with Methionine: " + str(True))
                else:
                        print("Sequence starts with Methionine: " + str(False))
#percentage of serine
                res_count = i.count('S')
                percent = round((res_count/length)*100)
                print("Serine percentage of this sequence: " + str(percent) + "%")
                count +=1
        total= len(seq)
        print("The number of sequence: " + str(total))
#sequence that have furin sites
def     RSVAS(seq, head):
        out = open("RSVAS.faa", 'w')
        for i in seq:
                for j in head:
                        if "RSVAS" in i:
                                out.write(j)
                                out.write(i + "\n")
        print("Check for RSVAS.faa where sequences containing RSVAS are allocated")

length(sequence)
RSVAS(sequence, header)
        
