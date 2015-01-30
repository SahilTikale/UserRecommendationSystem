#Movie Recommendation System for data mining project
#Preprocessing steps
#3.) Calculating similarity between users
import csv
import sys
import re
import string
from scipy import spatial

#def calCosineSimilarity(EachUser):


f = open(sys.argv[1])	#read the new ratings file
flines = f.readlines()
print len(flines)

wf = open("similarityScore.csv", "w")

##Calculating Pairwise cosine distance.

for i in range(1, len(flines)-1):	#For every candidate rating
	output = [0]*3
	a = flines[i].split(',')
	output[0] = a[0]
	del a[0]
	a_rating = [float(x) for x in a]	# Get a list of ratings

	for j in range(i+1, len(flines)):		#For every subsequent candidate rating
		b = flines[j].split(',')	  	

		output[1] = b[0]

		del b[0]
		b_rating = [float(x) for x in b]	#Get a list of ratings


		cosdist = 1 - spatial.distance.cosine(a_rating, b_rating)
		if(cosdist > 0.59):
			output[2] = round(cosdist, 4)
			print "Calculating score of", output[0],"with", output[1], "is:", output[2]
			sim_score = ','.join(map(str, output))
			wf.write(sim_score)
			wf.write("\n")
		else:
			pass


wf.close()

