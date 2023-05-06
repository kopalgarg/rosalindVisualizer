import matplotlib.pyplot as plt

def reverse_complement(dna_sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_seq = dna_sequence[::-1]
    return ''.join([complement.get(nucleotide, '') for nucleotide in reverse_seq])
dna_sequence = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

reverse_complement_sequence = reverse_complement(dna_sequence)
print(reverse_complement_sequence)