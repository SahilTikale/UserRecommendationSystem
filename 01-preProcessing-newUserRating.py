#Movie Recommendation System for data mining project
#Preprocessing steps
# 1.) Calculate the average of user rating
# 2.) Re-adjusting the user ratings based on this average
import csv
import sys
import re
import string
#import numpy as np


##Function definitions

def userAvgRating(allpairs):

	itemrate = []
	ratings = []
	for eachpair in allpairs:
		eachpair = eachpair.replace('(', '')
		eachpair = eachpair.replace(')', '')
		itemrate = eachpair.split(',')
		if len(itemrate) <= 1:
			pass
		else:
			ratings.append(float(itemrate[1]))
	avg = sum(ratings)/float(len(ratings))
	
	return round(avg, 4)



allUserAvgList = ["UserAverageRating"]


f = open(sys.argv[1])  #read the file
flines = f.readlines() #split it to list of lists


#Calculating Average of ratings by each user and saving it to file. 
wf = open("avgUserRating.csv", "w")
wnewRate = open("newUserRating.csv", "w")

wf.write("User-ID,Average-Rating")
wf.write("\n")

for line in flines:  	#for each line (or row) from file. 
	line = line.replace('\n', '')
	allpairs = line.split()  
	avgRate = userAvgRating(allpairs)
	avgRateMap = []
	avgRateMap.append(allpairs[0])
	avgRateMap.append(avgRate)
	allUserAvgList.append(avgRate)
	
#	print avgRateMap
	x = ','.join(map(str, avgRateMap))
#	print x	
	wf.write(x)	
	wf.write("\n")
# print allUserAvgList 	#In Addition to writing the user Averages to a file. I decided to collect them
						#also, in a list so that I can use them later if the need be. 





	movies = []
	newRating = [0]*3001	#Initializing an empty list with 3001 elements.
	print "length of list - newRating", len(newRating)
	newRating[0] = allpairs[0]	#User id as the first element.
	userLoc = int(allpairs[0].replace('U', ''))
	print userLoc
	
	for eachpair in allpairs:
		eachpair = eachpair.replace('(', '')
		eachpair = eachpair.replace(')', '')
		item_rate = eachpair.split(',')
		if len(item_rate) <= 1:
			pass
		else:
			movies.append(int(item_rate[0].replace('M', '')))	#This is used to seek the position of the rating in the list of newRatings
				
			userAvg = allUserAvgList[userLoc]
#			print "allUserAvgList[userLoc]", allUserAvgList[userLoc]
#			print "userAvg", userAvg
			newRate = float(item_rate[1]) - userAvg

			newRating[movies[len(movies)-1]] = round(newRate, 4)

	print "length of newRating after updates:", len(newRating)
	y = ','.join(map(str, newRating))
	wnewRate.write(y)
	wnewRate.write('\n')

			


wf.close()
wnewRate.close()
