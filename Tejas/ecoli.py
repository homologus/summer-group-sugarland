x = open("GCA_000005845.2_ASM584v2_genomic.fna", "r")
count = 0
y = x.read()

for i in range(69, len(y), 3):
	if(y[i:i+3] ==  "AGC"):
		count = count+1

print(count)
