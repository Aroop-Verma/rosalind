
fasta_f = open("C:\\Users\Magnolia\Downloads\\rosalind_cons.txt", "r")


def parse_fasta(fasta):

    fasta = fasta_f.readlines()
    
    seq_dict = {}

    for strings in fasta:
        if strings.startswith(">"):
            seq_id = strings[1:].rstrip()
            seq_dict[seq_id] = ''
        else:
            seq_dict[seq_id] += strings.strip()

    return seq_dict


def get_max_len(seq_dict):
    
    max_len = 0
    for value in seq_dict.values():
        current_len = len(value)
        if current_len > max_len:
            max_len = current_len
    
    return max_len


def compute_pos_id(fasta):

    seq_dict = parse_fasta(fasta_f)
    max_len = get_max_len(seq_dict)

    profile_dict = {}

    index = 0
   
    while index < max_len:

        for seq in seq_dict.values():

            if index in profile_dict:
                profile_dict[index].append(seq[index])
            else:
                profile_dict[index] = [seq[index]]

        index += 1

    # Now to construct a consensus sequence 
    
    count_dict = {}
    
    consensus = []
    
    A_list = []
    C_list = []
    G_list = []
    T_list = []

    for values in profile_dict.values():
        count_dict["A"] = values.count("A")
        count_dict["T"] = values.count("T")
        count_dict["G"] = values.count("G")
        count_dict["C"] = values.count("C")
        
        for key, value in count_dict.items():
            match key:
                case "A":
                    A_list.append(value)
                case "C":
                    C_list.append(value)
                case "G":
                    G_list.append(value)
                case "T":
                    T_list.append(value)


        max_count = 0
        for nt, count in count_dict.items():
            if count > max_count:
                max_count = count
                max_nt = nt 
        
        consensus.append(max_nt)

    return (consensus, A_list, C_list, G_list, T_list)

consensus_ , a, c, g, t  = compute_pos_id(fasta_f)
print(''.join(consensus_))
print(f"A: {' '.join(map(str, a))}")
print(f"C: {' '.join(map(str, c))}")
print(f"G: {' '.join(map(str, g))}")
print(f"T: {' '.join(map(str, t))}")