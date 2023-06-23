"""
Author: Edward Gregg
Class: CMSC206 Fall 2021
Project: Project 5B
Due Date: 20211114
"""

#https://www.loginradius.com/blog/async/beginners-guide-to-tweepy/
from textblob import TextBlob
# For parsing tweets
import tweepy

# Importing the NaiveBayesAnalyzer classifier from NLTK
from textblob.sentiments import NaiveBayesAnalyzer

from matplotlib import pyplot as plt, patches
import numpy as np


consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = '14864036-3RbrFndQQ9nH6g6LkMylcV5YHsQ8RVolPsKyT6nUa'
access_token_secret = 'dgyF4HLMVyBJqmzwJyTW8PSxgmJwYg6CyPIaXOP39crqo'
api_key = '2PVqirfZP1TBavo1U7LS137Rf'
api_secret = '1cSo3dpf5MyCbOblsBHE2LNAgoLOvfQ2ZsSnfSm8OH94v3eZWU'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAABxCVgEAAAAADbwihzv8RH0oOCgC58RuRHS77PQ%3D3MdzM5aADVDuRkkUDlWZxs2XvOsgMMa2sF1gbIaE8JCW41gslq'

# Establishing the connection
twitter = tweepy.OAuthHandler(api_key, api_secret)
api = tweepy.API(twitter)

'''
# This command will call back 5 tweets within a “lockdown” topic
#This is an example
corpus_tweets = api.search_tweets(q="lockdown", count=5)
for tweet in corpus_tweets:
    print(tweet.text)

# Applying the NaiveBayesAnalyzer
blob_object = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
# Running sentiment analysis
analysis = blob_object.sentiment
print(analysis)
'''
master_lst = []


###############################################
# First Person to Analyze                     #
###############################################
userID = "BarackObama"
BarackObama_lst = []
user_twitter = api.user_timeline(screen_name = userID, count = 15, include_rts = False)
pos = 0
neg = 0
for tweet in user_twitter:
    print(tweet.text)
    # Applying the NaiveBayesAnalyzer
    blob_object = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
    # Running sentiment analysis
    analysis = blob_object.sentiment
    print(analysis[0])
    BarackObama_lst.append(analysis[0])
    if analysis[0] == 'pos':
        pos += 1
    elif analysis[0] == 'neg':
        neg += 1

print(BarackObama_lst)
BarackObama_lst = [pos,neg]


###############################################
# Second Person to Analyze                    #
###############################################
userID = "TitusNation"
TitusNation_lst = []
user_twitter = api.user_timeline(screen_name = userID, count = 15, include_rts = False)
pos = 0
neg = 0
for tweet in user_twitter:
    print(tweet.text)
    # Applying the NaiveBayesAnalyzer
    blob_object = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
    # Running sentiment analysis
    analysis = blob_object.sentiment
    print(analysis[0])
    TitusNation_lst.append(analysis[0])
    if analysis[0] == 'pos':
        pos += 1
    elif analysis[0] == 'neg':
        neg += 1

print(TitusNation_lst)
TitusNation_lst = [pos,neg]


#################################################
# Third Person to Analyze                       #
#################################################
userID = "AOC"
AOC_lst = []
user_twitter = api.user_timeline(screen_name = userID, count = 15, include_rts = False)
pos = 0
neg = 0
for tweet in user_twitter:
    print(tweet.text)
    # Applying the NaiveBayesAnalyzer
    blob_object = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
    # Running sentiment analysis
    analysis = blob_object.sentiment
    print(analysis[0])
    if analysis[0] == 'pos':
        pos += 1
    elif analysis[0] == 'neg':
        neg += 1
    AOC_lst.append(analysis[0])


print(AOC_lst)
AOC_lst = [pos,neg]

#create data for plotting
# x_values = [AOC_lst[0],AOC_lst[1]]
# y_values = ['AOC']
# plt.bar(y_values,x_values, color = "blue")

# labels = ['AOC']
#
# x = np.arange(len(labels))
# width = 0.35 #width of bars
# #y = [AOC_lst[0]]
# y = [7]
# #z = [AOC_lst[1]]
# z = [2]
#
# ax = plt.subplot(111)
# ax.bar(x - width/2, 'AOC', y, width, color='b')
# ax.bar(x + width/2,'AOC', z, width, color='g')
# ax.set_xlabel('x-axis')
#
# plt.show()


langs = ['Barack Obama', "Titus" , 'AOC']

#langs_index = [x for x in range(len(langs))]  ##langs_index = [0, 1, 2, 3, 4, 5, 6]

BARACK = [BarackObama_lst[0], BarackObama_lst[1]]
TITUS = [TitusNation_lst[0], TitusNation_lst[1]]
CORTEZ = [AOC_lst[0],AOC_lst[1]]

# Pie chart
slices = [BarackObama_lst[0],BarackObama_lst[1], TitusNation_lst[0], TitusNation_lst[1], AOC_lst[0], AOC_lst[1]]
labels = ['Barack Obama Positive', 'Barack Obama Negative', 'Christopher Titus Positive', 'Christopher Titus Negative', "AOC Positive", "AOC Negative" ]
plt.pie(slices, labels = labels, autopct='%1.1f%%', wedgeprops={'edgecolor' :'black'})
plt.show()


# user_tweets = api.search_users(q="lockdown", count=5)
# for tweet in corpus_tweets:
#     print(tweet.text)
