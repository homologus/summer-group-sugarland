import re
x=open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna", "r")

skip = x.readline()

temp = x.read()
dnaarr = re.findall("\S", temp)
dna = ""
for a in dnaarr:
	dna+=a
#print (dna)

def translate(dna2):

	genecode = {
	    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
	    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	   'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
	    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
	protein = ""
	for i in range(0, len(dna2),3):
		if i < len(dna2)-3:
			codon = dna2[i:i + 3]
			#print (codon)
			protein = protein + genecode[codon]
	#print (protein)
	return protein

print(translate(dna))
