dna = str(str(open("C:\\Users\Magnolia\Downloads\\rosalind_revc(6).txt", "r").read()))

dna = dna.strip()
seq_len = 0 - (len(dna))

dna_rev = []
i = 0
while i >= seq_len:
    dna_rev.append(dna[i])
    i = i - 1

dna_rev = ''.join(dna_rev)

dna_rev_complement = []

index = 0
while index <= len(dna_rev)-1:
    match dna_rev[index]:
        case "A":
            dna_rev_complement.extend("T")
        case "T":
            dna_rev_complement.extend("A")
        case "G":
            dna_rev_complement.extend("C")
        case "C":
            dna_rev_complement.extend("G")
    index=index+1

dna_rev_complement_str = ''.join(dna_rev_complement)

print(dna_rev_complement_str)

print(len(dna), len(dna_rev), len(dna_rev_complement_str))
print(set(dna), set(dna_rev), set(dna_rev_complement_str))
print