f = open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna", "r")
skip = f.readline()
a = "".join(f.read().splitlines())


print(a[189:255])
