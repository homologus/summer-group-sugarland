from Bio import SeqIO

reads = list(SeqIO.parse("/share/SARS/seq.fasta", "fasta"))

aastring = str(reads[0].seq.translate())

split = aastring.split("*")

for i in range(0, len(split)):
  if(len(split[i]) >= 100):
    print(split[i], "\n")


