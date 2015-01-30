#Movie Recommendation System for data mining project
#Preprocessing steps
#5.) Predicting the rating for the movies for a given user.
# for every movie fetching the users list that have rated it. 
import csv
import sys
import re
import string
import linecache
import re

start = int(sys.argv[1])
end = int(sys.argv[2]) + 1
fname = "%s%s%s%s%s" % ("results/newNeighbors", start, "_to_", end-1, ".csv")

f = open("newSimScore.csv", "r")

flines = f.readlines()

wf = open(fname, "w")

#Generating queries

a = "U"
b = ","



for i in range(start, end):
	x1 = "%s%s%s" % (a, i, b)
	x2 = "%s%s%s%s" % (b, a, i, b)	
	neighbors = []
	for line in flines:
		if re.match(x1, line):
			word = line.split(',')
			neighbors.append(word[1])
		elif x2 in line:
			word = line.split(',')
			neighbors.append(word[0])
	z = ','.join(map(str, neighbors))
	wf.write(z)
	wf.write('\n')
	wf.flush()

f.close()
wf.close()
