file = open("C:\\Users\Magnolia\Downloads\\rosalind_dna(3).txt", "r")

seq = []

for i in file.read():
    seq.append(i)

count = []
count.append(seq.count("A"))
count.append(seq.count("C"))
count.append(seq.count("G"))
count.append(seq.count("T"))

c_str = ' '.join(map(str, count))
print(c_str)