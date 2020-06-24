from Bio.Seq import Seq
import random
from array import *

def randomprotein(percentage):
	inp = percentage
	length = 10000

	gcpercent = float(inp)/100
	atpercent = 1-gcpercent
	gcthou = int(length*gcpercent) 
	atthou = int(length*atpercent)


	seq = ""

	goodlen = True
	while goodlen:

  		rand = random.uniform(0,1)

  		if(rand >= 0 and rand < gcpercent/2):
     	 		seq += "G"
  		elif(rand >= gcpercent/2 and rand < gcpercent):
      			seq += "C"
  		elif(rand >= gcpercent and rand < 1-(atpercent/2)):
      			seq += "A"
  		elif(rand  >= 1-(atpercent/2) and rand <= 1):
      			seq += "T"

	  	if(len(seq)==10000):
    			goodlen = False

	seq = Seq(seq)
	seq = seq.translate()
	split = seq.split("*")

	for i in range(0, len(split)):
  		largest = ""
  		if(len(split[i]) > len(largest)):
    			largest = split[i]


	return(len(largest))

def average(a):
	total = 0
	for i in [a]:
		for j in range(0, 100):
			total += randomprotein(i)


	return(total/100)

arr = []
for c in range(20, 65, 5):
	print("Average Longest Length of Size ", c, ": ", average(c))
