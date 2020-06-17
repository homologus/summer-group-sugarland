from Bio import SeqIO

x = list(SeqIO.parse("seq.fasta", "fasta"))

print(len(x))
