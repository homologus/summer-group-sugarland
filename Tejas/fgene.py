from Bio import SeqIO

reads = list(SeqIO.parse("/share/SARS/seq.fasta", "fasta"))

aastring = str(reads[0].seq.translate())
aastring2 = str(reads[0].seq[1:].translate())
aastring3 = str(reads[0].seq[2:].translate())
split = aastring.split("*")
split2 = aastring2.split("*")
split3 = aastring3.split("*")

print("\nFirst Frame\n")
for i in range(0, len(split)):
  if(len(split[i]) >= 100):
    print(split[i], "\n")

print("Second Frame\n")
for i in range(0, len(split2)):
  if(len(split2[i]) >= 100):
    print(split2[i], "\n")

print("Third Frame\n")
for i in range(0, len(split3)):
  if(len(split3[i]) >= 100):
    print(split3[i], "\n")
