from Bio.Seq import Seq
import random

print("What is the GC percentage? (0-100)")
inp = int(input())
length = 10000

gcpercent = float(inp)/100
atpercent = 1-gcpercent
gcthou = int(length*gcpercent) 
atthou = int(length*atpercent)

numa = random.randint(0, atthou)
numt = int(atthou)-int(numa)
numc = random.randint(0, gcthou)
numg = int(gcthou)-int(numc)

seq = ""

goodlen = True
while goodlen:

  rand = random.randint(0,3)

  if(rand == 0 and numa != 0):
    seq += "A"
    numa -= 1
  elif(rand == 1 and numc != 0):
    seq += "C"
    numc -= 1
  elif(rand == 2 and numg != 0):
    seq += "G"
    numg -= 1
  elif(rand == 3 and numt != 0):
    seq += "T"
    numt -= 1

  if((numa + numt + numg + numc) == 0):
    goodlen = False

seq = Seq(seq)
seq = seq.translate()

split = seq.split("*")

for i in range(0, len(split)):
  largest = ""
  if(len(split[i]) > len(largest)):
    largest = split[i]


print(len(largest))
