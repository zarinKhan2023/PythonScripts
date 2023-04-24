#!/usr/bin/env python3

# import argparse library
import argparse

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
for line in lines:
    if not line.startswith('>'):
        sequence.append(line.rstrip())
#converts lower to upper
def     convertUP(seq):
        for i in seq:
                UC = i.upper()
        print("The uppercase of this file content is: " + UC)
#count the valine
def     count_V(seq):
        for i in seq:
                v_counter = i.count('V')
        print("The number of Valine in the sequence is : " + str(v_counter))
#count trypotophan
def     count_W(seq):
        for i in seq:
                W_counter = i.count('W')
        print("The number of Trypotophan in the sequence is : " + str(W_counter))
#the length of the sequence
def     length_seq(seq):
        for i in seq:
                length = len(i)
        print("The length of the sequence is : " + str(length))
#count the polar nuetral side-chains
def     polar_count(seq):
        for i in seq:
                polar_count = i.count('S') + i.count('N') + i.count('T') + i.count('Q')
        print("The total polar neutral side-chains count in the sequence is " + str(polar_count))
#replace all trytophans with gycine
def     replace_W(seq):
        for i in seq:
                replace_w = i.replace('W','G')
        print("Replacing Tryptophan with Glycine:\n" + replace_w)
#print
convertUP(sequence)
count_V(sequence)
count_W(sequence)
length_seq(sequence)
polar_count(sequence)
replace_W(sequence)
