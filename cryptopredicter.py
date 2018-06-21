#! usr/bin/env python3

'''
Utilizes sentiment and opinion analysis to guess how future coins will change
Takes into account positive/negative opinions, and also people's bias
Analyses your own twitter, must follow crypto news to be helpful

High level Idea:
	1. Scrape Reddit for N/E/B info, and use sentiment analysis
	2. Scrape Twitter ^^^^
	3. Combine the results of these and use some math to get an overall score
	4. After this, we'll use past trends and estimation lines to see how these match up 
	5. Maybe train a neural net to see how accurate score and estimation lines were
	   with past trends that already exist
'''

import tweepy
import praw
from textblob import TextBlob


#-----------Twitter Init--------------
myKey = '***'
mySecret = '***'
accessToken = '***'
tokenSecret = '***'

auth = tweepy.OAuthHandler(myKey, mySecret)
auth.set_access_token(accessToken, tokenSecret)
api = tweepy.API(auth)

neoTweets = api.search('Neo')
ethTweets = api.search('Ethereum')
bitTweets = api.search('Bitcoin')
neoScore, ethScore, bitScore = 0, 0, 0

#------------Reddit Init---------------
reddit = praw.Reddit(client_id='***', 
					 client_secret='***',
					 password='***', 
					 user_agent='***', 
					 username='***' 
					 )
neoSub = reddit.subreddit('Neo')
topNeo = neoSub.hot(limit=50)
for post in topNeo:
	tAnalysis = TextBlob(post.title)
	dAnalysis = TextBlob(post.selftext)
	tPolarity = tAnalysis.sentiment.polarity
	tSubject = tAnalysis.sentiment.subjectivity
	dPolarity = dAnalysis.sentiment.polarity
	print(tPolarity,dPolarity)

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
