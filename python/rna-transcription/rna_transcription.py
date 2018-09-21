def to_rna(dna_strand):
    dna = ""
    for letter in list(dna_strand):
        if(letter == 'G'):
            dna = dna + "C"
        if(letter == 'C'):
            dna = dna + "G"
        if(letter == 'T'):
            dna = dna + "A"
        if(letter == 'A'):
            dna = dna + "U"
    return dna
