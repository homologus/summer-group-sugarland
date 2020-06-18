from Bio import SeqIO
reads = list(SeqIO.parse("seq.fasta", "fasta"))

print(reads[0].seq[100:200])
