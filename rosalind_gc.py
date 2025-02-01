def parse_fasta(fasta):
    fasta_dict = {}
    current_label = None

    for line in fasta.splitlines():
        if line.startswith('>'):
            current_label = line[1:].strip()
            fasta_dict[current_label] = ''
        else:
            fasta_dict[current_label] += line.strip()
    
    return fasta_dict

def gc_content(dna):
    if len(dna) == 0:
        return 0.0
    gc_content = dna.count('G') + dna.count('C')
    return (gc_content / len(dna)) * 100

def highest_gc(fasta_file):
    fasta_dict = parse_fasta(fasta_file)

    max_gc_id = None
    max_gc_content = 0.0

    for seq_id, dna in fasta_dict.items():
        current_gc_content = gc_content(dna)
        if current_gc_content > max_gc_content:
            max_gc_content = current_gc_content
            max_gc_id = seq_id
    
    return max_gc_id, max_gc_content

fasta_file =  open("C:\\Users\Magnolia\Downloads\\rosalind_gc.txt", "r").read()

result_id, result_gc_content = highest_gc(fasta_file)
print(result_id)
print(result_gc_content)