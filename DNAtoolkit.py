nucleotides = ["A", "G", "C", "T"]


# Check the squance to make sure it is a DNA
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    tempFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tempFreqDict[nuc] += 1
    return tempFreqDict
