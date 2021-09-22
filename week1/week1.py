import string

code = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R','GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

dna_seq ='ATGCTTGCAAATACGTCACGACAGTGAAAAA'
comp = string.maketrans('ATGC', 'UACG')
rna_seq = (dna_seq[3:12] + dna_seq[17:23])[::-1].translate(comp)
aminoacid_seq = ''

for i in range(0,len(rna_seq),3) : aminoacid_seq+=code[rna_seq[i:i+3]]

print 'dna_seq = \"' + dna_seq + '\"'
print 'rna_seq = \"' + rna_seq + '\"'
print 'aminoacid_seq = \"' + aminoacid_seq + '\"'