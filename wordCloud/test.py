

import requests
import bs4 as bs
import pandas as pd
import re

source = requests.get('http://www.debates.org/index.php?page=debate-transcripts').content

soup = bs.BeautifulSoup(source,'html.parser')

content = soup.find(id='content-sm')

firstdebatelink=[]

for link in content.findAll('a'):
    if 'The First' in link.string:
        firstdebatelink.append(link.get('href'))

for link in content.findAll('a'):
    if 'The First' in link.string:
        print(link.get('href'))

title=[]

for link in content.findAll('a'):
    if 'The First' in link.string:
        title.append(link.string)

df = pd.DataFrame(columns=title)

nospacechars = []

for i in firstdebatelink:
    source = requests.get(i).content
    soup = bs.BeautifulSoup(source,'html.parser')
    content = soup.find(id='content-sm')
    count = content.find('p').text
    count = count.replace('\n', '')
    nospacechars.append(len(re.sub(r"\s+", "", count)))

war_count=[]

for i in firstdebatelink:
    source = requests.get(i).content
    soup = bs.BeautifulSoup(source,'html.parser')
    content = soup.find(id='content-sm')
    count = content.find('p').text
    a = re.split(r'\W', count)
    b = a.count('wars')+a.count('Wars')+a.count('war')+a.count('War')
    war_count.append(b)

from collections import Counter

most_common_w=[]



for i in firstdebatelink:
    source = requests.get(i).content
    soup = bs.BeautifulSoup(source,'html.parser')
    content = soup.find(id='content-sm')
    count = content.find('p').text
    words = re.findall(r'\w+', count)
    cap_words = [word.upper() for word in words]
    word_counts = Counter(cap_words)
    mostcommon = word_counts.most_common(1)
    most_common_w.append(mostcommon[0][0])

most_common_w_count=[]

most_common_w_count

df.loc[1] = nospacechars
df.loc[2] = war_count
df.loc[3] = most_common_w
df.loc[4] = most_common_w_count

df['Name']=['Debate char length','war_count','most_common_w','most_common_w_count']

df.set_index('Name')
