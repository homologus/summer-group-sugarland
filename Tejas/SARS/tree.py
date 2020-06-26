from Bio import SeqIO

bat = list(SeqIO.parse("/share/SARS/bat-sars-genome.fa","fasta"))

print(bat[0].seq.translate())
