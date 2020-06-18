from Bio import SeqIO

x = list(SeqIO.parse("/share/SARS/seq.fasta","fasta"))
NSeq=x[0].seq

#first frame
PSeq= NSeq[0:len(NSeq)//3*3].translate()
PSeq.split("*")
for ele in PSeq:
        if(len(ele)>=100):
                print("frame " + str(i)),
                print(ele),
                print(" "),

#second frame
sNSeq=NSeq[1:(len(NSeq)//3*3)-2]
PSeq= sNSeq.translate()
PSeq.split("*")
for ele in PSeq:
        if(len(ele)>=100):
                print("frame 2:"),
                print(ele),
                print(" "),
            
#third frame
tNSeq=NSeq[2:(len(NSeq)//3*3)-1]
PSeq= tNSeq.translate()
PSeq.split("*")
for ele in PSeq:
        if(len(ele)>=100):
                print("frame 3:"),
                print(ele),
                print(" "),



