import matplotlib.pyplot as plt

def transcribe(dna_sequence):
    return dna_sequence.replace('T', 'U')

def plot_rna_sequence(rna_sequence):
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, rna_sequence, fontsize=20, ha='center', va='center')
    ax.axis('off')
    plt.show()

dna_sequence = 'ATGCTGATCG'

rna_sequence = transcribe(dna_sequence)

plot_rna_sequence(rna_sequence)