file_path = "C:\\Users\Magnolia\Desktop\code\\rosalind_grph.txt"

def parse_fasta(file_path):

    return open(file_path, "r").readlines()


def seq_dictionary(file_path):

    FASTA = parse_fasta(file_path)

    seq_dictionary = {}

    for line in FASTA:
        if line.startswith(">"):
            seq_id = line[1:].strip()
            seq_dictionary[seq_id] = ''
        else:
            seq_dictionary[seq_id] += line.strip()   

    return seq_dictionary


def indexed_dict(file_path):

    dict = seq_dictionary(file_path)
    
    indexed_list = []

    index = 1

    for value in dict.values():
        indexed_list.append(value)
        index+=1

    return indexed_list


def match_sequences(file_path, minimum_match_k = 3):

    indexed_list_sequences = indexed_dict(file_path)

    overlap_graph = {}

    index = 0
    while index < len(indexed_list_sequences):
        
        current_sequence = indexed_list_sequences[index]
        index+=1    
        
        for seq in indexed_list_sequences:
            
            if  current_sequence != seq:
                s_suffix = current_sequence[-minimum_match_k:]
                t_prefix = seq[:minimum_match_k]
                
                if s_suffix == t_prefix:
                    suffix_sequence = current_sequence
                    prefix_sequence = seq

                    if suffix_sequence in overlap_graph:
                        overlap_graph[suffix_sequence].append(prefix_sequence)
                    else:
                        overlap_graph[suffix_sequence] = [prefix_sequence]
                    
    return overlap_graph


def build_output_dict(file_path):
    fasta = seq_dictionary(file_path)
    overlap = match_sequences(file_path)

    for s, t in overlap.items():
        for value in t:
            for fasta_id, fasta_seq in fasta.items():
                if value in fasta_seq:
                    t_id = fasta_id
                    t_seq = fasta_seq
                elif s in fasta_seq:
                    s_id = fasta_id
                    s_seq = fasta_seq
            print(s_id, t_id, sep = ' ')


build_output_dict(file_path)



    

