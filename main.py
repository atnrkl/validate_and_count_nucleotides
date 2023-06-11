from DNAtoolkit import *
import random


rndDNAstr = "".join([random.choice(nucleotides) for nuc in range(20)])

DNAstr = validateSeq(rndDNAstr)

print(countNucFrequency(DNAstr))
