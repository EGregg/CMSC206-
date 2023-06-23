# Author: Edward Gregg
# Class: CMSC206 Fall 2021
# Project: Group Project Question 3
# Due Date: 20211209

import requests
import bs4 as bs
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt
import csv
import numpy as np

source = requests.get('http://www.debates.org/index.php?page=debate-transcripts').content

soup = bs.BeautifulSoup(source,'html.parser')

content = soup.find(id='content-sm')

theDebate=[]

for link in content.findAll('a'):
    if '2020' in link.string:
        theDebate.append(link.get('href'))

print(theDebate)

for link in content.findAll('a'):
    if '2020' in link.string:
        print(link.get('href'))

title=[]

for link in content.findAll('a'):
    if '2020' in link.string:
        title.append(link.string)

print(title)

df = pd.DataFrame(columns=title)

print(df)


nospacechars = []

for i in theDebate:
    source = requests.get(i).content
    soup = bs.BeautifulSoup(source,'html.parser')
    content = soup.find(id='content-sm')
    count = content.find('p').text
    count = count.replace('\n', '')
    nospacechars.append(len(re.sub(r"\s+", "", count)))

print(nospacechars)


############################################################################
#Count how many times covid of pandemic comes up
############################################################################

covid_count=[]

for i in theDebate:
    source = requests.get(i).content
    soup = bs.BeautifulSoup(source,'html.parser')
    content = soup.find(id='content-sm').text
    #count = content.find('p').text
    #a = re.split(r'\w', count)
    #b = a.count('covid')+a.count('pandemic')+a.count('Covid19')+a.count('COVID-19')
    #covid_count.append(b)
    final = content.count('COVID-19') + content.count('COVID') + content.count('coronavirus') + content.count('virus') + content.count('pandemic')
    covid_count.append(final)

print(covid_count)


############################################################################
#Setup the dataframes
############################################################################


df.loc[2] = covid_count


df['Name']=['covid_count']

df.set_index('Name')

pd.options.display.max_colwidth = 10
print(df.set_index('Name'))


def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(15, 10))
    # Display image
    plt.imshow(wordcloud, interpolation = 'bilinear')
    # No axis details
    plt.axis("off");
    plt.show()

# Import image to np.array
#mask = np.array(Image.open('stormtrooper_mask.png'))

# Generate wordcloud
stop_words = ["Trump", "Biden", "re", 's', 't', 'welker'] + list(STOPWORDS)
wordcloud = WordCloud(width = 2000, height = 1000, random_state=1, background_color='black', colormap='rainbow', collocations=False, stopwords = stop_words).generate(content)

# Plot
plot_cloud(wordcloud)
