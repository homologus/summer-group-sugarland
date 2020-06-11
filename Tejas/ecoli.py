'''
Created on Jun 11, 2020

@author: TrexK
'''

x = open("GCA_000005845.2_ASM584v2_genomic.fna", "r")
skip = x.readline()
y = x.read()


proteins = {"Alanine" : 0, "Arginine" : 0, "Asparagine" : 0, "Aspartic Acid" : 0, 
            "Cysteine" : 0, "Glutamic Acid" : 0, "Glutamine" : 0, "Glycine" : 0, 
            "Histidine" : 0, "Isoleucine" : 0, "Leucine" : 0, "Lysine" : 0, 
            "Methionine" : 0, "Proline" : 0, "Serine" : 0, "Threonine" : 0, 
            "Tryptophan": 0, "Tyrosine" : 0, "Valine" : 0 }

for i in range(0, len(y), 3):
        if(y[i:i+3] ==  "GCG" or "GCA" or "GCC" or "GCT"):
            proteins["Alanine"] += 1
        if(y[i:i+3] == "CGC" or "CGT" or "CGG" or "CGA" or "AGA" or "AGG"):
            proteins["Arginine"] += 1
        if(y[i:i+3] == "AAC" or "AAT"):
            proteins["Asparagine"] += 1
        if(y[i:i+3] == "GAT" or "GAC"):
            proteins["Aspartic Acid"] += 1
        if(y[i:i+3] == "TGC" or "TGT"):
            proteins["Cysteine"] += 1
        if(y[i:i+3] == "GAA" or "GAG"):
            proteins["Glutamic Acid"] += 1
        if(y[i:i+3] == "CAA" or "CAG"):
            proteins["Glutamine"] += 1
        if(y[i:i+3] == "GGG" or "GGA" or "GGT" or "GGC"):
            proteins["Glycine"] += 1
        if(y[i:i+3] == "CAC" or "CAT"):
            proteins["Histidine"] += 1
        if(y[i:i+3] == "ATT" or "ATC" or "ATA"):
            proteins["Isoleucine"] += 1
        if(y[i:i+3] == "ATG" or "ATA" or "CTT" or "CTA" or "CTG" or "CTC"):
            proteins["Leucine"] += 1
        if(y[i:i+3] == "AAA" or "AAG"):
            proteins["Lysine"] += 1
        if(y[i:i+3] == "ATG"):
            proteins["Methionine"] += 1
        if(y[i:i+3] == "CCA" or "CCG" or "CCT" or "CCC"):
            proteins["Proline"] += 1
        if(y[i:i+3] == "AGT" or "AGC" or "TCG" or "TCT" or "TCC" or "TCA"):
            proteins["Serine"] += 1
        if(y[i:i+3] == "ACT" or "ACC" or "ACA" or "ACG"):
            proteins["Threonine"] += 1
        if(y[i:i+3] == "TGG"):
            proteins["Tryptophan"] += 1
        if(y[i:i+3] == "TAC" or "TAT"):
            proteins["Tyrosine"] += 1
        if(y[i:i+3] == "GTG" or "GTA" or "GTC" or "GTT"):
            proteins["Valine"] += 1
          

for key, value in proteins.items():
    print("%s : %s\n" %(key, value))
