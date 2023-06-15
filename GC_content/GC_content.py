def calculate_gc_content(dna_string):
    """Calculates the GC-content of a DNA string."""
    gc_count = dna_string.count('G') + dna_string.count('C')
    return gc_count / len(dna_string)

# Read in the DNA strings from the FASTA files
fasta_file = open('rosalind_gc.txt')
dna_strings = {}
current_id = ''
for line in fasta_file:
    if line.startswith('>'):
        # Start of a new DNA string
        current_id = line[1:].strip()
        dna_strings[current_id] = ''
    else:
        # Append the current line to the current DNA string
        dna_strings[current_id] += line.strip()

# Calculate the GC-content for each DNA string
gc_contents = {}
for id, dna_string in dna_strings.items():
    gc_contents[id] = calculate_gc_content(dna_string)

# Find the ID of the string with the highest GC-content
max_id = max(gc_contents, key=gc_contents.get)

# Output the result
print(max_id)
print('{:.6f}'.format(gc_contents[max_id] * 100))
