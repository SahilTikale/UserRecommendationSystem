#Movie Recommendation System for data mining project
#Preprocessing steps
#5.) Predicting the rating for the movies for a given user.
# for every movie fetching the users list that have rated it. 
import csv
import sys
import re
import string
import linecache


#FUNCTIONS 

def fetchMovieRating(user, movie):

#	print "User is", user		#trace logic
#	print "Movie is", movie		#trace logic
	
	x = linecache.getline('newUserRating.csv', int(user))
	x = x.strip("\n")
	y = x.split(',')

	return float(y[int(movie)])

def fetchSimScore(user1, user2):
	if user1 > user2:
		user3 = user2
		user2 = user1
		user1 = user3
	
#	print "user1 is ", user1	#trace logic
#	print "user2 is ", user2 	#trace logic
	userpair = "%s%s%s%s%s%s" % ('U', user1, ',', 'U', user2, ",")

#	print userpair				#trace logic

	with open("newSimScore.csv") as simi:
		for line in simi:
			if userpair in line:
				line = line.strip('\n')
				x = line.split(',')
#				print x				#trace logic
#				print x[2]			#trace logic
#				print type(x[2])	#trace logic
				y = float(x[2])
#				print "Sending simScore to program: ", y	#trace logic
				return y
				break

def hasSeenMovie(movieid):
	x = linecache.getline("movieNeighbors.csv", int(movieid))
	x = x.strip('\n')
	y = x.split(',U')
	del y[0]
	z = [int(b) for b in y]
	return z

def areNeighbors(uid):
	x = linecache.getline("newNeighbors.csv", int(uid))
	x = x.strip('\n')
	y = x.split(',U')
	del y[0]
	z = [int(b) for b in y]
	return z	

inbegin = int(sys.argv[1])
inend = int(sys.argv[2])

begin = inbegin + 1
end = inend + 2

fname = "%s%s%s%s%s" % ("results/", inbegin, "_to_", inend, ".csv")
#print fname

f = open(fname, "w")

for i in range(begin, end):
	result = []
	a = linecache.getline('mapping.csv', i)
	a = a.strip("\n")
	b = a.split(',')
#	print b				#trace logic
	result.append(b[0])
	uid = int(b[1])
	mid = int(b[2])
#	print result[0], "User is:", uid, mid 	#trace logic

## ** Fetching average User Rating for user in question ** ##

	ua = linecache.getline('avgUserRating.csv', uid+1) 	#ua = user,average
	ua = ua.strip('\n')
	ual = ua.split(',')
	avgrate = float(ual[1])			# -- (value 1)
#	print "Average rate of user", ual[0], "is", avgrate, type(avgrate)	#trace logic

## ** Fetching common Users who have seen the movie and are neighbor to target users. 
	seenList = hasSeenMovie(mid)
#	print "User who saw the movie", seenList	#trace logic
	isaneighbor = areNeighbors(uid)
#	print "User who saw movie and are neighbor to", uid, isaneighbor #trace logic
	neighborWhoSawit = list(set(seenList)&set(isaneighbor))
#	print "Common user list: ", neighborWhoSawit 	#trace logic
	

#	print "People who have seen this movie", seenList
## ** Fetching the similarity score for each user 
	simUser = [] 	#List of top similar user who have seen the movie	
	peerRate = []	#Rating given by similar user to the movie
	simScore = []	#Similarity score of top users 
		
	if (len(neighborWhoSawit) > 15):
		lp = 15
	else:
		lp = len(neighborWhoSawit)

	for i in range(lp):
		if (len(simScore) < 8):
			score = fetchSimScore(uid, neighborWhoSawit[i])
			if (score is not None):
				simScore.append(score)
#				print "neighborWhoSawit:", neighborWhoSawit[i]	#trace logic
#				print "simScore at line 105: ", simScore		#trace logic
				pr = fetchMovieRating(neighborWhoSawit[i], mid)
				peerRate.append(pr)
#				print "Similar users found: ", len(simScore)	#tracelogic
			else:
				pass
		else:
			break

#	print "Top five similar user to user ", uid, "are", simUser
#	print "Total similar Users found: ", sum(simUser)
#	print "Their similarity score for", uid, "is" , simScore
#	print "Their rating of movie is ", peerRate 
	
# ** Calculating the recommendation.  **

#Product of respective simScore and ratings of the movie in question

	peerOpinion =  [a*b for a,b in zip(simScore,peerRate)]
	totPeerOpinion = sum(peerOpinion)

#	print "peerOpinion is ", peerOpinion, "sum is ", sum(peerOpinion)

	totSimScore = sum(simScore)
#	print "Adjust for all similarity: ", totSimScore

	reco = avgrate + (totPeerOpinion/totSimScore)
	reco = round(reco, 4)

#print "Recommendation of Rating of movie", "%s%s", ('M',mid), "for user", "%s%s", ('U', uid)
#print "Recommended Rating: ", reco
	x = "%s%s%s%s" % (result[0], ",", reco, "\n")
	f.write(x)
#	f.flush()

f.close()


				


