#!/usr/bin/python3
f = open("pUC19c.fasta")
fc = f.readlines()
seq = []
#join the sequence
for i in range(1, len(fc)):
        seq.append(fc[i].strip("\n"))
seq = "".join(seq)
print(seq)
#count the number of SMAI sites "CCCGGG"
def     SMAI_count():
        SMAI = seq.count("CCCGGG")
        print("SMAI sites: " + str(SMAI))
#content of AT
def     AT():
        AT = (seq.count("A")) + (seq.count("T"))
        AT_content = round(AT/ (len(seq))*100)
        print("AT content: " + str(AT_content))
#content of GC
def     GC():
        GC = (seq.count("G")) + (seq.count("C"))
        GC_content = round(GC/ (len(seq))*100)
        print("GC content: " + str(GC_content))
#calling the functions
SMAI_count()
AT()
GC()
