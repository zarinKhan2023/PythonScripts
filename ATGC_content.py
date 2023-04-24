#!/usr/bin/env python3

# import argparse library
import argparse
import re

# create parser object
parser = argparse.ArgumentParser()

# create argument group
required = parser.add_argument_group('Required arguments')

# add argument to group
required.add_argument('-i', '--input', type=str,
                      help='Path to input file', required=True)

# parse the arguments into variables
args = parser.parse_args()

# open file
file_in = open(args.input)

# read file contents
lines = file_in.readlines()
sequence = []
header = []
# just sequence
for line in lines:
        if not line.startswith('>'):
                sequence.append(line.removesuffix("\n"))
        else:
                header.append(line)
#Calculate AT and GC repeat
def     count_AT(seq):
        AT = 0
        for i in seq:
                AT += i.count("AT")
        print("The number of AT in the fasta file: " + (str(AT)))
#function to count GC
def     count_GC(seq):
        GC = 0
        for i in seq:
                GC += i.count("GC")
        print("The number of GC in the fasta file: " + (str(GC)))
#count the length of each sequence
def     length(seq):
        count = 0
        for i in seq:
                count += seq.count(i)
                print("The length of line " + str(count) + " is")
                print((i.count('A'))+(i.count('T'))+(i.count('G'))+(i.count('C')))
def     EcoR1(seq):
   eco = 0
        for i in seq:
                eco += i.count("GAATTC")
        print("Number of EcoR1 sites: " + str(eco))
        #Calculate AT and GC content of the sequence
def     content_ATGC(seq):
                length = len(seq)
                countA = seq.count('A')
                countT = seq.count('T')
                countG = seq.count('G')
                countC = seq.count('C')
                AT = round(((countA + countT)/length)*100)
                GC = round(((countC + countG)/length)*100)
                print("The percent of AT content:\n"+ str(AT) + "%")
                print("The percent of GC content:\n"+ str(GC) + "%")
count_AT(sequence)
count_GC(sequence)
length(sequence)
EcoR1(sequence)
content_ATGC(sequence)
