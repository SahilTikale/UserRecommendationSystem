#Movie Recommendation System for data mining project
#Preprocessing steps
#4.) Calculating similarity between users
# for every movie fetching the users list that have rated it. 
import csv
import sys
import re
import string
from scipy import spatial


f = open(sys.argv[1])
flines = f.readlines()

wf = open("movieNeighbors.csv", "w")

#Fetching the movie neighbors. 
a = "("
b = "M"
d = ","

thisMovie = []
movieName = []
for i in range(1, 3001):
	x = "%s%s%s%s" %(a, b, i, d)
	y = "%s%s" %(b, i)
	thisMovie.append(x)
	movieName.append(y)



for m in range(len(thisMovie)):
	movieNeighbor = []
	movieNeighbor.append(movieName[m])
	for line in flines:
		if thisMovie[m] in line:
			allpairs = line.split()
		 	movieNeighbor.append(allpairs[0])
			
	z = ','.join(map(str, movieNeighbor))
	wf.write(z)
	wf.write("\n")

wf.close()


