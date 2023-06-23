# Author: Edward Gregg
# Class: CMSC206 Fall 2021
# Project: Group Project Question 2
# Due Date: 20211209

import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

file = 'us-states.csv'
file2 = 'historical_state_counts.csv'

# df = pd.read_csv(file)
# state_grouped = df.groupby('state', sort = 'True')
# florida_grouped = state_grouped.get_group('Florida')
# print(florida_grouped)

############################################################
#Prison cases df
############################################################

prison_df = pd.read_csv(file2)
#print(list(prison_df.columns))
state_death_df = prison_df[['Date','State','Residents.Confirmed','Residents.Deaths']]
prison_grouped = state_death_df.groupby('State',sort='True')
Maryland_grouped = prison_grouped.get_group('Maryland')
#print(Maryland_grouped[['Date','State','Residents.Confirmed']])
Maryland_date_residents = Maryland_grouped[['Date','State','Residents.Confirmed']]
Maryland_date_residents = Maryland_date_residents.fillna(0)
#print(Maryland_date_residents)
Maryland_date_residents.plot(x='Date',y='Residents.Confirmed')
#plt.show()
#Maryland_confirmed = prison_grouped.get_group('Maryland').max()['Residents.Confirmed']



############################################################
#State cases df
############################################################

df = pd.read_csv(file)
grouped = df.groupby('state')
state_Maryland = grouped.get_group('Maryland')
#state_Maryland.plot(x="date", y="cases", title="Number of total COVID-19 cases");
#plt.show()


Maryland_residents = Maryland_grouped[['Date','Residents.Confirmed']]
state_Maryland_cases = state_Maryland[['date','cases']]
state_Maryland['date'] = pd.to_datetime(state_Maryland['date'])
print(state_Maryland.info())
print(type(state_Maryland['date']))

Maryland_grouped['Date'] = pd.to_datetime(Maryland_grouped['Date'])
print(type(Maryland_grouped.info()))
print(state_Maryland_cases)

#ax = Maryland_residents.plot(x = 'Date', y = 'Residents.Confirmed')
#state_Maryland_cases.plot(ax=ax, x ='date', y = 'cases')
#plt.show()



#############################################################
#CreateFigure
#############################################################

fig = plt.figure(figsize = (12,6))


############################################################
#Create Axes
############################################################
ax = fig.add_subplot(111, label = '1')
ax2 = fig.add_subplot(111, label = '2', frame_on = False)

#########################################################
#Attempting to fix the tick marks -- Not working
#########################################################
#x = np.random.randint(low=0, high=1, size=50)
#y = np.random.randint(low=0, high=1, size=50)
# ax.set_xticks(np.arange(0, len(x)+1, 12))
# ax.set_yticks(np.arange(0, max(y), 48))
# ax2.set_xticks(np.arange(0, len(x)+1, 12))
# ax2.set_yticks(np.arange(0, max(y), 48))

############################################################
#Set parameter first Axes
############################################################
ax.bar(x = Maryland_grouped['Date'], height = Maryland_grouped['Residents.Confirmed'], color = 'C1')
ax.set_xlabel('Date', color = 'C1')
ax.set_ylabel('New Coronavirus Cases - State', color = 'C1')
ax.yaxis.tick_right()
ax.yaxis.set_label_position('right')
ax.tick_params(axis = 'x', color = 'C1')
ax.tick_params(axis = 'y', color = 'C1')
plt.xticks(rotation=90)

############################################################
#Set parameter second Axes
############################################################
ax2.plot(state_Maryland['date'], state_Maryland['cases'], color = 'C0')
ax2.set_xlabel('Date', color = 'C0')
ax2.set_ylabel('New Coronavirus Cases - Prison', color = 'C0')
ax2.xaxis.tick_top()
ax2.xaxis.set_label_position('top')
#plt.xticks(rotation=90)

############################################################
#Display
############################################################
plt.tight_layout()
plt.show()

#this group simply groups each states
#print(df)

# #this grouped returns the max covid cases for each State
# grouped = df.groupby('state', sort=True).max().reset_index()
