def to_rna(dna_strand):
    rna = ''
    for char in dna_strand:
        if char == 'C':
            rna += 'G'
        if char == 'G':
            rna += 'C'
        if char == 'T':
            rna += 'A'
        if char == 'A':
            rna += 'U'
    return rna
