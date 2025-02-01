rna = str(open("C:\\Users\Magnolia\Downloads\\rosalind_rna.txt", "r").read())
rna = rna.rstrip()
rna = rna.replace("T", "U")
print(rna)