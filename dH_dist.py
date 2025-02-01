
hamm_f = open("C:\\Users\Magnolia\Downloads\\rosalind_hamm(1).txt", "r").read()

seq_list = hamm_f.split()

seqA = seq_list[0]
seqB = seq_list[1]

print("Length of Seqeunce A:",len(seqA), "Length of Sequence B:",len(seqB))

i = 0
dH_dist = 0

while i < len(seqA):
    print(i)
    if seqA[i] == seqB[i]:
        i = i + 1
    else:
        dH_dist = dH_dist + 1
        i = i + 1

print(dH_dist)