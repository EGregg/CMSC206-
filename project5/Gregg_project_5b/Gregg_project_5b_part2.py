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
import csv #Import csv
import pandas as pd
import regex as re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import csv


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


# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

userID = "BarackObama"
for tweet in api.user_timeline(screen_name = userID, count = 15, include_rts = False):
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.text.encode('utf-8')])
    #print (tweet.created_at, tweet.text)

userID = "TitusNation"
for tweet in api.user_timeline(screen_name = userID, count = 15, include_rts = False):
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.text.encode('utf-8')])
    #print (tweet.created_at, tweet.text)

userID = "AOC"
for tweet in api.user_timeline(screen_name = userID, count = 15, include_rts = False):
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.text.encode('utf-8')])
    #print (tweet.created_at, tweet.text)

csvFile.close()

##########################################
# Data Cleaning
##########################################
df = pd.read_csv('result.csv', header = None, usecols = [0]) #loads csv file into pandas dataframe
df = df.astype(str)
print(df.dtypes)
text = ''
for string in df:
    print (type(string))

with open('result.csv', 'r+') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if len(row) != 0:
            print (type(row[0]))
            text += row[0]
            print (text)

pd.options.display.max_colwidth = 200
#df.head() #prints out first few columns in a dataframe
df.shape #prints the shape of dataframe

#a = df.loc[1].to_string() #loads the row from dataframe
#print(a)

# regex_pattern = re.compile(pattern = "["
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                            "]+", flags = re.UNICODE)
# match = re.sub(regex_pattern,'',a) #replaces pattern with ''
# #print(match)
#
# #a = df.loc[1].to_string()
# #print(a)
#
# pattern = re.compile(r'(https?://)?(www\.)?(\w+\.)?(\w+)(\.\w+)(/.+)?')
# match = re.sub(pattern,'',a)
# #print(match)
#
# #a = df.loc[1].to_string()
# #print(a)
#
# re_list = ['@[A-Za-z0–9_]+', '#']
# combined_re = re.compile( '|'.join( re_list) )
# match = re.sub(combined_re,'',a)
# #print(match)
#
# # stopwords = set(STOPWORDS)
# # stopwords.update(["elonmusk","elon musk","elon","musk","spacex"])


wordcloud = WordCloud(width = 600, height = 600, random_state=1, background_color='black', colormap='rainbow', collocations=False, stopwords = STOPWORDS).generate(text)
# Set figure size
plt.figure(figsize=(100, 100))
# Display image
plt.imshow(wordcloud, interpolation = 'bilinear')
# No axis details
plt.axis("off");

#show the word cloud
#plt.show()

# Save image
wordcloud_save_as = "wordcloud_mask.png"
wordcloud.to_file(wordcloud_save_as)
print("The word cloud is being generated as" , wordcloud_save_as)
