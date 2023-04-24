#!usr/bin/python3
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
list_seq = sequence
#counts the repeats of AT in sequence
def     countAT(seq):
        count_AT = seq.count("AT")
        print("The number of AT repeats in the sequence is:\n" + str(count_AT))

#counts the repeats of GC in sequence
def     countGC(seq):
        count_GC = seq.count("GC")
        print("The number of GC repeats in the sequence is:\n" + str(count_GC))
#EcoR1 count
def     countEco(seq):
        count_E = seq.count("GAATTC")
        print("The number of EcoR1 sites in the file is:\n" + str(count_E))
def     EcoCut(seq):
        cutting_EcoR1 = seq.replace('AATTC'," " + 'AATTC')
        cutting_EcoR1 = cutting_EcoR1.split(" ")
        print("The sequences post EcoR1 cutting: ")
        print(cutting_EcoR1)
#print
countAT(list_seq)
countGC(list_seq)
countEco(list_seq)
EcoCut(list_seq)
