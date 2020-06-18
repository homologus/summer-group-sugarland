#Open the file
#make a for loop running from a range of 0 to 2
#translate each frame
#inside for loop, split sequence by _ , then remove strings shorter than 100

from Bio import SeqIO

x = list(SeqIO.parse("/share/SARS/seq.fasta","fasta"))
NSeq=x[0].seq

#for i in range(0,3):
#	NSeq= NSeq[i:(len(NSeq)//3*3)-i]
#	PSeq= NSeq.translate()
#	PSeq.split("*")
#	for ele in PSeq:
#		if(len(ele)>=100):
#			print("frame " + str(i)),
#			print(ele),
#			print(" "),

