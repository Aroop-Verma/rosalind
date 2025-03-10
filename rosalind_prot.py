import re

#codon_table = open("C:\\Users\Magnolia\Desktop\code\\rna_table.csv", "r").read()
#print(codon_table)

cod_file = open("C:\\Users\Magnolia\Desktop\code\\rna_table.txt", "r").read()
codon_Table = cod_file.strip()

codon_Table = re.sub(" {2,}", ";", codon_Table)
codon_Table = re.sub("\n", ";", codon_Table)

codon_Table = codon_Table.split(";")

codons = {}

for elements in codon_Table:
    element_break = elements.split(" ")
    if element_break[1] in codons:
        codons[element_break[1]].append(element_break[0])
    else:
        codons[element_break[1]] = [element_break[0]]


RNASEQ = "AUGAAUAACUACAAUGACUCCCUUUAUUUAUCUUAUGCCCUUUCCAAACGGAGGGGGGUGACCAAUGUAUACUCACAAUCCCGCAUUACAGCGCCGGAACCGGCCUCGUUAAGCGCACCUCCCUAUCUUCUCCGAGUAUUUCUAAGCUUAGCAAAGUGCCUCGGUCUUGUCUGUCUUAACAGCCAAGCCGUGACGGAUGAGAUGGCUAUGUGGAGGGAACCAGCAGAAAAAUAUUUCACCAGGUCGACUACGGACAUGCCGGCCAGUAGCGCCGCUAUGGUUUGUAUCUGUGUGAAACGAAGCUCACUCAAGGGCUGGAAUCGCAAAAAUCUGGCAGGGCUGUCUAGCGAGAACAUCGAAAAAAUUGAAAAAGUCAUCCCGCCACUCUAUGUUCAAGGAAAAAUGUUACUAGUCUUAAUAGUUACUUUCUCGCGGCGGACGAUUAUAUUGUUAUACUCCAUCCCCCAGGACAACGCGGUGGUUAACGAUUCGGCAGUGCUAUUAACAGCAACCACCAUGGGGUGUCGCCUGGAGGACUCCACGCACUAUCUGACCUAUACAACCAGAUUUACAGGAACCGACAUUAGGAGAGCCACUCUAGUACUCCCGGUAUACCCAUGCAGCCGCAUAGGCACGCACUUCUCGUUCCCCUUCAUUACCAACUAUUCCCAUGAGUUCAAAUCAAUAAUUAUGCAACCCAAAAGUUGGAAAAAGUAUGAGAAGACACCUGGUGUUCCUGGCCGUGAGUUGGGUAACAAAACAUCUGAUGGCAUAAAGUCCUGCCGCUGUGGCGGGGAACAGAUUGCUGGGCUCGGUGGAUACAUGCAUAAACUCAGUGCGCGCUGUAGUCGGUCCCGCCUCCAUCACGGGCAUCUUUCUGCGGCUCUUAAAUUAUGCUUUAAACCCAUUAGAUGUUUACCCAGCAAAGGUCGAGGGAUGUUCGUAGAGGAAGGACUAGGUAGGAUUGGCCCUCGUUACUGCAGUCGUUUGCGGGCAUUAAAACAUUUUAGUUCGUUUGCUAUCCACUGUCCGCAUGAUACAUUUAUCGUGUUAAUGCUAUUCAAGACUCGCUCUAUAAACAAUAUACUCGUCCCUCGUUACGGUGUUGGCAGACGAACCGUCACACGAGGGAACAAAAGGAAUGCACCGGUCCGCUGCCCGGCGUUUCAACCUAACUUUAUGGCACCAGACGCGCGUGCAAUUAAGAAUAACACUGAUGUGAAGACUAUGUUAGCAUGUGCAUUCUAUCUUAACUUGAUGGCCCGGAACGACGUCCAGAAAAGGUCUUCCGGCGGUCCAGCAUAUUGCGGCAUUAAGCAAGAAAGGGCCUCUAGUGAAGAACCGUUGUCCCUUGCGCGGACGAUGCGCCUGGAUCCCCUCAUGUACUUCCCGGUCCUGUCUGCCGUACGCGUAGUGUCGACUACAGAGAGUGACGCCUGUCUUCGAUCACGUUACUCUGACUCAGCCAUCCAUGUCAGGAAGAUGGUUAGGCUUCGAGAAGAACAUUUACCACCGACCAAUUGUACUCAAUCAGCUACGUUCAGGAAAGGCACGGCUACACAUACUCUGCCCGCAGUACCCCGCUCUUCCGAUACCAAGCUAGAGCCGCGUCUCUUGGCCCAUCCACCUCGAUUCGGCGUUGAUAUUGUCCAACGAUUGUUUCUUGCAACCCUCCGCUUAUUUCUCACUAACAUGAUUGGGGACUCCUAUCGUAUGCACCGAUACCCGGUUACACACGAACGGUUCUUCUGUAGUGAGACAGUGCCGCAGCUGGAACCUGAAGCGCCCUCCCGGACACAGACCAAGCGCGGUUACUGGCCUCCGCUUGCGGCAUUACUCUUGACGAAUUGGAGCACAUCAACCUGGCUAGAUCGGUUUCGCGCACAGGCUGACCCCGCAUCCCAGUACUGCCCGGUGAGUGGGAAGUAUUGGUCAUGCUGCCCAGGCUCAGCAACGGAACCAUGGUAUAUUCGCGGUUACUCCAUGCAGAACCCUCGCAUAUUGGUCUUGCCGUUGCAUCAUUGCAGCUUUAUGCGGUAUAGGCCACCUUUUGCAGUAGUGCACGUGUGCUCCACACGGACAUCCGGCAGAAUGUUGCAACCAGACAUCUUGACUCGGCUCGGUCAUCGAUGGCAAAGGAGAAGGUGCAUCCUAUUCCGGACAUGUCUUAAUCGUGCGCUUCUAGGGAAUAUUAUGACAGUGAGCGGGAGACACUACAGGUGCAAAGUCAUCGUCAGUCCCCUUCUAGGGUCUCUAAAAGUCCGAAUGGCGGCUGCCCAGCGAGAGAUGUUAAAGAUUGAUCCUGAGGAUCCCAACGCAGAACAAUGUUGGUCUCGGACUCUAUCACUGCCCCACGCUUGGGUAAGAUACCCCUGCUGGCUGAACUCUGAAAGACUCUCUAUAUGUAUGCUGCCCCCGACGUUCUACUACAGUUCCGCUGCUGAUGCAAACCUUUCCGUCAGGGGGUGGUGCAUUUCAUACCUAAAGGCGAGCUACUGUUAUCGCUCCAACAUCAUGUCACCGCAUAGUUCGAUAAGGGUCUAUUACGGGUUUCCCUGCCGACACUCGCUAGCACGGCCUACCCGGUCCUACGCAGUCGAAUUUUGCGCAAGAAUUCCAACUCCUAGAAUGCAGUCCCAGCCAAUACCUACUUACUCUCCGAUGGAAGUGCCAUCAAUGGCGGCGUGUUCUAUACGACCCAAGUCGUGCACAUUGAUGCGCACACCCCCAUUUAGUCGUGUGGAUGGAGGGUUAUUUAACAUGACUCCUGUAGUUCAAUCCCGGUACAUCCGGCUCGUUCUUAAGGGGCGAGGCUCUCCCCCUAGCCGCUACGAGGAAGCAAUCAGGGGUAUGGGAUUGAUCUUAAGAGUACUAGCCCCCUUCUCAACGUUCUCUACACUCGCAUGGCUUUUUGGCACGAGGCAGUCCAUGAGAGAAGGGGAGCUGGACGUCUGGUCGUACAGUCGGCUCCCGACAAAAAGACGACGCGCGGCGUAUUUUCCUGUAACCACUACAAGUGUGGACGAGGUUCGCGACAAUCUGUUCACGUGUGUUUAUAUCUGGCGGACUGAGCGCCAACGCAUUAAGAUCCCUCUACCCCAACUGCUGGCGUACUUCGUGAGUAUUAUCAUUAGGGCAACCCACUCCGGUGUCUCCGUACGCCCGCGCACUACGGAGCUUGCAGGCACUGGACGCGGGGUUCAGCCUGGCCAUGCUUCCGCUGGAUAUAGCUCUUCAAUCCGCACGUACGUUAUCACAAGCAAGAAGUCGAUUCGCAUCCUGCGCAACCCUUACCUUAGACCUUUGAUGUUAGCCACCGCGGUCGGCCUCUACAGAAACCUUCCUCGAAGGGAUACGGCGGUAUGUGGCCGUAUCUCUACCCCCUGGGCACUGAGAUAUAUAGCCCUGUCGAGUGCAUUGUCCACUUGGCAGUGGCCAAUGCUUUCCGCGUACCCCACCGUGACGCUCGCCGAUUUACAUUGGCCUUAUGACAUCUCCCAGCAUUCCAAUGUAGCGUCACGGAGGAUCCCCGAGACAAUGAACCCCGAGAUCCGACACCGACUCCUAGAACGUAUGAAGUCCCAUGUGGUCGUAUCCCGACACACGUGUUUCGAAAAAGAGCUGGCUCCAGGCUACUCUUCUGUUUGUGAAACGUCAUGGAACCUUCUAGUCUAUCCGCAGACUGGUUCGGGAUCUGGUGCAGUGAUGAUUCGCUCAGCUCCAUCGCGUAGCAGGUGUGAAUCUUUGGAACUGUCCGGCUACGAUUUCUUUAGCAUCUGUCUACGAAACAAACGUUAUUUUUGUGUGAGGAGAACAGGUGGGUCCGACCCGGCACAUCUAAUUGCAGGACUAGACUACUUAUUUGGCCGUCAUUCCAUGGCACUCCAGAUGGGGCUUCCUAUCUUUGGGGUCCUGGGGCCACUGAAGGCCGGAAGACGUAAAUCCCCCAGGACAACCUGGAGCCGAUUCGGAGAUAUGCCCCGUCUCUCUAAAACCCUUUGUGAUCUAUUCACCGCCACCUUCGUCACCACUUUCGUCAAUCUAUUACGUAGGACUUCUCUGGCUGCAUUGCCACCCGGACUUCAGCUUUUUAACGUGGGCUACACUUACUCUUUUCGCUCUCAAGAUAUUACUUCCUUGGAUGAAGAGGAACGCAUGUUUACGCAUGGCAGACGGCGUGAAGCCACCACGUCGCAACCUGCUCUCAAGAUAAGAAAUAACGACGGGGUUGACAGACAGGGGUCCCAGCUGGCUGCGCCAUACUUGCUUACCGCACUAAGAAAUCUCCAUUGGCCUGAAAAAGCCCUCGAUCACUACCCAACCUGUGGCACUUGGCCCCUAGGUAUACAGUACGACGUAGGACGGGCGUUCCACACAUUGGUUCAGCCGCGGGACCAACGUAACGUGCUCAAAAUUCUCCGCCCCCGCUACUCUACUCAACUUAACCUGGAUAUUCAACCUGCGUACUUUGCUUCCACUAAAACAAAUAAGAAAUUCGAGGGGUUGCAAAUCGCUGAUACCAGGCAUGGCGUUUGUAUGCGAGGGGUAGUUACGACCGCGUGUGGGUUGGAUCCAAAGGUCCCUCGGCAAAGGACUGAUUCUUGGGUUGCAAUGCCCCGACCAAGUUGCCCCCCGGCUCAUGGCUUCGUUGAGCGGCUUCCUGCCGCCUUAUCGUCCGGAACAACACGACGAGCUCUUACCGUUAAACUAUUCUUAUACCACGUUUGGCUAAGGCUCGGUGAAAUUUAUGGAGGCAUCGCGCCGCGACUUCACCUUGAGCACGUGUGCAAAACAAAAUCGCGACGGCUGGUUCGCAUAAUGGGUUUCGAGUGGUUAGAGCACUGGACAUUAGAGGCAACGCCCGCUGGCAGCUGUACAUUAGACGUCCUCCUGCGGAGGAAUACGAGCUUUAUAGAUUAUAGCUCAGCUGUGAAACAAUCAUUCACUCUAGCGAAAGUGCUAAUUCCGCAACCGUGGAUAUGCCGUACAAGAUAUCCUUACCGACGGAACUUGAGCGCGCUCCCUCUAAGGACCAUGCGCAGAACCAUUGGAACUCAGUUAUUCCCUACUCGACGUAUUGAGUCACGUGUCAAAGGAACAGAUUUUAAAUAUCUCGCCGUUACGCGGACGAAAGCACAUUUUUUCACAAAUGGUGUGUAUAAAAUCCCGAGCGAGGGGGGCAUAACUUCAGUGUUAAAGCAUUUGGCAUCAAGCUAUUGUCUGAUCGCACACUCUUGUUCCCUUUUUGUGGUCAAUUAUACAGCUUUGUACGACCGUGUACGAGCUAGCCAUCAGUUUGACCAUGGUGACGCAAUGAAAGCGUUGCUUAGUCUUGUUUAUUUUUAUUCACUAGGUUACUCAAUUCGCCAACGGAACUCACAACAUAAACGUCUCGCUGUUCAAGGUAUUAACGGACCAGUGAUCAUCGUUAGAUCUCCACAAUGGUCCGGUCCCAAUAGGGUGACGUUAACCAAGGGUCUCAGUUUGCGCAAGGGUCGUUGCAGCGUCUUUCACUACGUAUAUGGCCAAUCCGAAUCACAGGAGCACGCAUACGGCCCUUGGACAUGGCCGUUUCGUAAUCCAGUGGACUCUCGUCAUUUUAUUGAGUACUCCUCCCGGUGUUUAUUGCCGCCUACGCGUCCCCGCAUAAAUUCGCGACUACAGUGGAGGACCCUUUCGAAUAUAGUGAAAUGUAAUUACCCCACAGCAUUGUCCGCCUUAAGUUUCACUGAAUAUGCGUUGAUCCUCAAGGAUCCCCCUAGUGCCAGGCUCGGUUCUGGGACAAUGAGUGCACCCGAUUCAGAUAGGCGGCUCGACGAGGCACUGCCAGGUGGACUGCGAGAAGGUCAUUCUGGGAUUAGACUUCUGAGGGCUUGCCACAUCGAUUGCCGGAGGGCGCAUGCAGCGACCAGUCUUAAGCGUGAUGUGGUAGCAAUCACACCGGGUCCACGCGGAUCGCCCCGGAAGAGUUUUGCCGGUUACCCGGGGAUUCCCCAUCAACCUAAUGCUUGCUUGGGAAACCGCAUAAUAACCCGCUCAUGUCGUCAACGAGGACCGAAGGGAUGCCACUGUCCUCUACACAUUCAUGUAGGGUGCGGGUCGGCUGGAGCCCAUGUGGCCUGCGAAAUCAUAAAUGUGUGGUGCGUACCGUUCGCACGCUCGAUCGUGUCGGUGCGCAGGGCUAGUAACGCGUUGCGUUGUAAAGACCUUAGAACUCUCUGGUUGCCAGGAUGGGCCGCGCGGAAGAUUCGAGCGUAUUCAAUUUUGAUACUCUGGGCCUCUGGUCAGACCGCUCACUGCCCCGGGCGUGUCCGCUCACUUGACGUAGUAACGAGUGGCUCAAACCUGCCGCGCUGCUUGUUCCGGGUAUUCGUCGAUUGUACGAGACGGAUAUCAGCGAUUGGUAAUGCUGUACAUUGCUCUCUGGUUUCCGGCCCGGUCCCUCAGUAUGAAGACGGGAGGUCCGAGGCAUCAUACAUCAGUAGACUGCAGGUAACAUUGGUCGAGGAGAGUGACAUAUUACAGAACGCUGUUUUACCGGUCGACCAAAGCAUCACCAUCGUUAGGACAGACCAGAUACGUUCGAGUUUCAUAUUGCUUUCUAAACCUUUACGCCUACCAACGCGCGUCACUAUAAUGGCAAAGAUAGACCAACCUGAUCCUCAAUGCGUAUUCGGCCAAAUCCAGGGCCGCCGUAACGCUCUCACAUGCGGAUCUGGGCCAUCGGGGUCAAGGGGGUUGGCCUGUAGUAACAUCACAGGGCCACUAAGGAGAUGUUGGAUCAGCAUGAUCCCAUAUACCCAACAAAUAAAUACCUGUAUUCGCACCGGUACGAGUCUACUAAUCGUCGUAGGUACGUGGAUACCGAACACGAUUUGGGAUGAGCAGGCCCAUAAUCAUCAAACGUGGAGGGGGAGUGUUUGUAUAAAUCUACUCUGGACCGUCAUGAAGGAACUGAGACCGGGUGAUGUUAGAAACGCCACCAAAAGACUAAUCCACCCCGAUUCAUACUGUCAAAACAGUACUCUCUUACUCUCAUGUCCCGGAUUUAAGCACGCUUGUGCGAAGGGCAACUCACUAGCCGAUAUCGCACUGUGUUGUGCAGAGCGGACUUCGUUCAGACGCGGGCAUCACGUGAACGCUCACUUAACGUCAAUCAUUGCAGUCUCACGGAGACUAACUGGUUCUAACGACUUUUUGGGACGCCAGUUGUUUGGAGUUCUAAUUGCAUUUCUGGGCGUUCGGGGAUUGUACUGCCUGCUUUAUUCGACUCGACGUGUUGAGUACAGGUGCGGUAAUGCAUUAGGUGCCCUCCCGGCUGAGUUCAUUCCCGCGAACUACCCUUUCUUUCAUUACCGCACGCCGAUUAGUCCUUCCCACCGAAUCGUUCGGUCAACUGAUCAUCUCCACCUUGACCGGUGCGCGGCUUUCGUGCAAUACAAAACUUCAGCUCAGCUGAGGGGCAUUGCAGCUGUCAGUAAUCACGUAAAUCCGCGGGGAUCCCGGUCGAACCACGCGUGCGUGUCAAUGGAAAUACGUGCCCGCGUUGGAAGAAACAUCUGUCGUUUAUGUCCAGGCAUGCUAGAGCCAGAUGACCUCCAAAGUGAGGGAGAGUCUACACCGCUCAAUGCGGGUUUGGCGCUCUGGGCUUCCUGCAAUAGAAACAACAAUUCUCAGAUUGGUGAAAGUACACUAGCGGUGUUGCCGAAUAGCACUAAUUCGCGUAAGAGUGAUGGACUAGGUCCUUAUUGCCUAUACAUCGGAUUGCGUACCUCACGGACGCAGAUAGACUGGGAAAUAUGGAGCACGGCGCAUUGGAUUCAAAGCGAUGAGUCCGCAAGCAAUUACGCCGGAGCGGAACGACCCUUAGGGGUUAAGGACAAGAGGGCGGGUAAAGAUACUCACGGGCAGGAAUCUUGCACUGGGUUGACAGCAGAAUACUGUGAGAAAGAUUUCACACAGGGGCCCUGCGUGGAGGUCCACAUGAUCCUCAGCGUUAAAUCUGGUCGGCCUAACGAGUCGGUGUUCGUCGUACGGCUCUAUAUGUAUAAAAGUGCCGUCAUAAACAUGCUGCAGUCCACCUAUGCAACGCAAGUUCCAUCUCCAUCUCAAUCGGGGCGUUCACAGAGAAGUAGCUAUUAUGGGUUCUAUUAUUCAAUGUUGCGGUUCCGCAAAACGGCCACCAGAGGAGGUUUAAUUGCAUCCGAACUUUGGCCAACGCAUGUGUCAGUUCCAGCCGGACGCGAGUCCCCAGUACUAGCUUCUGAAUAUGCUACGACUAGGCUCCCCCUCAUAUGCUGCAUGUGGUGCAAAGCAAGCAUCACAACUAUUACAAGAACAAACUGUGCUUCCUGGGGGCAUUCCGUAGUGAAGUUUAUACCGCGAAACGGCUAUCACGCCGGAUGCUUAUACGCACGUUCAAGUUGCAGACCGUUGCUCCGCGACUCUGCUUUCUACCGCCCCUCUUGGGUACAAAGGGCUCAAAAGCGCGCCGCGCGAACAGUUGGUCUUCCUAACUGGGCGAACACAAGGCCUCGCUCUGUGGAUGAUUUUAGUUCACGAGACGAGGCUGGAGGGCCUUCGACACCAAGACUCGGACGUGGGCACCAAUCGAAAUCAACCACUUUGACGGCCGUGAAUGUUGCCACGCGAAAAUAUAUAAGUAAUGUGACAGACAUCGAGUCUGCGUUGACUUGCGUUGGCCCGCAAGCCUCUGAUUCCUUAAGGCCUACGCUGAUCCACUCUAGCCCCCGUAAAAUGUAUCCUGGUGCGUAUUUUCGUCGUUCUACACUUAGUAGUCGUGUCAUGGCAGAACAAGAAGAGCUAAACGCGAAUCUCACGGCUUUUCUGUCACUACUAGUCUAUUAA"

def rnaseq_to_protein(sequence):
    
    protein = ""
    index = 0
    STOP = False

    while STOP == False:
        codon = sequence[index:index+3]

        for amino_ , codons_ in codons.items():

            for amino_codons in codons_:
                
                if codon in amino_codons:

                    if amino_ == 'Stop':
                        STOP = True
                    else:
                        protein += amino_ 
                    
        index+=3
    
    return protein

output = rnaseq_to_protein(RNASEQ)
print(output)
