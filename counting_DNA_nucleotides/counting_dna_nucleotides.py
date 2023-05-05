import matplotlib.pyplot as plt

def count_nucleotides(dna_sequence):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in dna_sequence:
        if nucleotide in counts:
            counts[nucleotide] += 1
    return counts

def plot_nucleotide_counts(dna_sequence):
    counts = count_nucleotides(dna_sequence)
    nucleotides = list(counts.keys())
    values = list(counts.values())
    plt.bar(nucleotides, values)
    plt.xlabel('nucleotides')
    plt.ylabel('count')
    plt.title('counts of nucleotides in DNA sequence')
    plt.show()

dna_sequence = 'ATGCTTCAGAAAGGTCTTACG'
plot_nucleotide_counts(dna_sequence)
