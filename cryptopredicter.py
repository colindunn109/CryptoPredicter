'''
Utilizes sentiment and opinion analysis to guess how future coins will change
Takes into account positive/negative opinions, and also people's bias
Analyses your own twitter, must follow crypto news to be helpful
'''

import tweepy
from textblob import TextBlob

myKey = 'rtMn5HeH9fvbsFjBVv7bqoOOA'
mySecret = 'nkm56LU8FEwRZdaoM3rIcuY252fx74TaG5CYXSpP2bkUpiuwzm'
accessToken = '923079179549097985-r1bdWg8OYvyHaLCHPkN6K16Xpx3YRJv'
tokenSecret = 'LgUaydtZqgTus5XcTyuCghDgaMmO6XQ0OCfuAQFnlw7pK'

auth = tweepy.OAuthHandler(myKey, mySecret)
auth.set_access_token(accessToken, tokenSecret)

api = tweepy.API(auth)

neoTweets = api.search('Neo')
ethTweets = api.search('Ethereum')
bitTweets = api.search('Bitcoin')
neoScore, ethScore, bitScore = 0, 0, 0

for tweet in neoTweets:
	analysis = TextBlob(tweet.text)
	currentPolarity = analysis.sentiment.polarity
	currentSubject = analysis.sentiment.subjectivity
	if(currentSubject == 0): #if its a fact, we want this to be heavily weighted
		currentSubject = 1
	if(currentSubject == 1): #if its an opinion, less weighted
		currentSubject = 0.1
 
	score = currentSubject * currentPolarity
	neoScore += score

for tweet in ethTweets:
	analysis = TextBlob(tweet.text)
	currentPolarity = analysis.sentiment.polarity
	currentSubject = analysis.sentiment.subjectivity
	if(currentSubject == 0): #if its a fact, we want this to be heavily weighted
		currentSubject = 1
	if(currentSubject == 1): #if its an opinion, less weighted
		currentSubject = 0.1
 
	score = currentSubject * currentPolarity
	ethScore += score

for tweet in bitTweets:
	analysis = TextBlob(tweet.text)
	currentPolarity = analysis.sentiment.polarity
	currentSubject = analysis.sentiment.subjectivity
	if(currentSubject == 0): #if its a fact, we want this to be heavily weighted
		currentSubject = 1
	if(currentSubject == 1): #if its an opinion, less weighted
		currentSubject = 0.1
 
	score = currentSubject * currentPolarity
	bitScore += score

print("Neo Score:" , neoScore)
print("Ethereum Score:" , ethScore)
print("Bitcoin Score:" , bitScore)
