# Author: Edward Gregg
# Class: CMSC206 Fall 2021
# Project: Group Project Question 1
# Due Date: 20211209

import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

#read the data and create a dataframe
file = 'us-states.csv'
df = pd.read_csv(file)

#This groups each state together and then finds the max of the state in each column
grouped = df.groupby('state', sort=True).max().reset_index()
print(grouped)

#Shows a graph with the total amount of cases per state
grouped.plot.bar(x="state", y="cases", title="Number of total COVID-19 cases");
plt.show(block=True);


grp = df.groupby('state')

bordering_alabama = grp.get_group('Florida').max()['cases'] + grp.get_group('Georgia').max()['cases'] + grp.get_group('Mississippi').max()['cases'] + grp.get_group('Tennessee').max()['cases']
bordering_alaska = grp.get_group('Alaska').max()['cases']
bordering_arizona = grp.get_group('California').max()['cases'] + grp.get_group('Colorado').max()['cases'] + grp.get_group('Nevada').max()['cases'] + grp.get_group('New Mexico').max()['cases'] + grp.get_group('Utah').max()['cases']
bordering_Arkansas = grp.get_group('Louisiana').max()['cases'] + grp.get_group('Mississippi').max()['cases'] + grp.get_group('Missouri').max()['cases'] + grp.get_group('Oklahoma').max()['cases'] + grp.get_group('Tennessee').max()['cases'] + grp.get_group('Texas').max()['cases']
bordering_California = grp.get_group('Arizona').max()['cases'] + grp.get_group('Nevada').max()['cases'] + grp.get_group('Oregon').max()['cases']
bordering_Colorado = grp.get_group('Arizona').max()['cases'] + grp.get_group('Kansas').max()['cases'] + grp.get_group('Nebraska').max()['cases'] + grp.get_group('New Mexico').max()['cases'] + grp.get_group('Oklahoma').max()['cases'] + grp.get_group('Utah').max()['cases'] + grp.get_group('Wyoming').max()['cases']
bordering_Connecticut = grp.get_group('Massachusetts').max()['cases'] + grp.get_group('New York').max()['cases'] + grp.get_group('Rhode Island').max()['cases']
bordering_Delaware = grp.get_group('New Jersey').max()['cases'] + grp.get_group('Pennsylvania').max()['cases'] + grp.get_group('Maryland').max()['cases']
bordering_florida = grp.get_group('Florida').max()['cases'] + grp.get_group('Alabama').max()['cases'] + grp.get_group('Georgia').max()['cases']
bordering_Georgia = grp.get_group('North Carolina').max()['cases'] + grp.get_group('South Carolina').max()['cases'] + grp.get_group('Tennessee').max()['cases'] + grp.get_group('Alabama').max()['cases'] + grp.get_group('Florida').max()['cases']
bordering_Hawaii = 0
bordering_Idaho = grp.get_group('Utah').max()['cases'] + grp.get_group('Washington').max()['cases'] + grp.get_group('Wyoming').max()['cases'] + grp.get_group('Montana').max()['cases'] + grp.get_group('Nevada').max()['cases'] + grp.get_group('Oregon').max()['cases']
bordering_Illinois = grp.get_group('Kentucky').max()['cases'] + grp.get_group('Missouri').max()['cases'] + grp.get_group('Wisconsin').max()['cases'] + grp.get_group('Indiana').max()['cases'] + grp.get_group('Iowa').max()['cases'] + grp.get_group('Michigan').max()['cases']
bordering_Indiana = grp.get_group('Michigan').max()['cases'] + grp.get_group('Ohio').max()['cases'] + grp.get_group('Illinois').max()['cases'] + grp.get_group('Kentucky').max()['cases']
bordering_Iowa = grp.get_group('Nebraska').max()['cases'] + grp.get_group('South Dakota').max()['cases'] + grp.get_group('Wisconsin').max()['cases'] + grp.get_group('Illinois').max()['cases'] + grp.get_group('Minnesota').max()['cases'] + grp.get_group('Missouri').max()['cases']
bordering_Kansas = grp.get_group('Nebraska').max()['cases'] + grp.get_group('Oklahoma').max()['cases'] + grp.get_group('Colorado').max()['cases'] + grp.get_group('Missouri').max()['cases']
bordering_Kentucky = grp.get_group('Tennessee').max()['cases'] + grp.get_group('Virginia').max()['cases'] + grp.get_group('West Virginia').max()['cases'] + grp.get_group('Illinois').max()['cases'] + grp.get_group('Indiana').max()['cases'] + grp.get_group('Missouri').max()['cases'] + grp.get_group('Ohio').max()['cases']
bordering_Louisiana = grp.get_group('Texas').max()['cases'] + grp.get_group('Arkansas').max()['cases'] + grp.get_group('Mississippi').max()['cases']
bordering_Maine = grp.get_group('New Hampshire').max()['cases']
bordering_Maryland = grp.get_group('Virginia').max()['cases'] + grp.get_group('West Virginia').max()['cases'] + grp.get_group('Delaware').max()['cases'] + grp.get_group('Pennsylvania').max()['cases']
bordering_Massachusetts = grp.get_group('New York').max()['cases'] + grp.get_group('Rhode Island').max()['cases'] + grp.get_group('Vermont').max()['cases'] + grp.get_group('Connecticut').max()['cases'] + grp.get_group('New Hampshire').max()['cases']
bordering_Michigan = grp.get_group('Ohio').max()['cases'] + grp.get_group('Wisconsin').max()['cases'] + grp.get_group('Indiana').max()['cases'] + grp.get_group('Minnesota').max()['cases']
bordering_Minnesota = grp.get_group('North Dakota').max()['cases'] + grp.get_group('South Dakota').max()['cases'] + grp.get_group('Wisconsin').max()['cases'] + grp.get_group('Iowa').max()['cases'] + grp.get_group('Michigan').max()['cases']
bordering_Mississippi = grp.get_group('Louisiana').max()['cases'] + grp.get_group('Tennessee').max()['cases'] + grp.get_group('Alabama').max()['cases'] + grp.get_group('Arkansas').max()['cases']
bordering_Missouri = grp.get_group('Nebraska').max()['cases'] + grp.get_group('Oklahoma').max()['cases'] + grp.get_group('Tennessee').max()['cases'] + grp.get_group('Arkansas').max()['cases'] + grp.get_group('Illinois').max()['cases'] + grp.get_group('Iowa').max()['cases'] + grp.get_group('Kansas').max()['cases'] + grp.get_group('Kentucky').max()['cases']
bordering_Montana = grp.get_group('South Dakota').max()['cases'] + grp.get_group('Wyoming').max()['cases'] + grp.get_group('Idaho').max()['cases'] + grp.get_group('North Dakota').max()['cases']
bordering_Nebraska = grp.get_group('Missouri').max()['cases'] + grp.get_group('South Dakota').max()['cases'] + grp.get_group('Wyoming').max()['cases'] + grp.get_group('Colorado').max()['cases'] + grp.get_group('Iowa').max()['cases'] + grp.get_group('Kansas').max()['cases']
bordering_Nevada = grp.get_group('Idaho').max()['cases'] + grp.get_group('Oregon').max()['cases'] + grp.get_group('Utah').max()['cases'] + grp.get_group('Arizona').max()['cases'] + grp.get_group('California').max()['cases']
bordering_NewHampshire = grp.get_group('Maine').max()['cases'] + grp.get_group('Vermont').max()['cases'] + grp.get_group('Massachusetts').max()['cases']
bordering_NewJersey = grp.get_group('Pennsylvania').max()['cases'] + grp.get_group('Delaware').max()['cases'] + grp.get_group('New York').max()['cases']
bordering_NewMexico = grp.get_group('Oklahoma').max()['cases'] + grp.get_group('Texas').max()['cases'] + grp.get_group('Utah').max()['cases'] + grp.get_group('Arizona').max()['cases'] + grp.get_group('Colorado').max()['cases']
bordering_NewYork = grp.get_group('Pennsylvania').max()['cases'] + grp.get_group('Rhode Island').max()['cases'] + grp.get_group('Vermont').max()['cases'] + grp.get_group('Connecticut').max()['cases'] + grp.get_group('Massachusetts').max()['cases'] + grp.get_group('New Jersey').max()['cases']
bordering_NorthCarolina = grp.get_group('Tennessee').max()['cases'] + grp.get_group('Virginia').max()['cases'] + grp.get_group('Georgia').max()['cases'] + grp.get_group('South Carolina').max()['cases']
bordering_NorthDakota = grp.get_group('South Dakota').max()['cases'] + grp.get_group('Minnesota').max()['cases'] + grp.get_group('Montana').max()['cases']
bordering_Ohio = grp.get_group('Michigan').max()['cases'] + grp.get_group('Pennsylvania').max()['cases'] + grp.get_group('West Virginia').max()['cases'] + grp.get_group('Kentucky').max()['cases'] + grp.get_group('Indiana').max()['cases']
bordering_Oklahoma = grp.get_group('Missouri').max()['cases'] + grp.get_group('New Mexico').max()['cases'] + grp.get_group('Texas').max()['cases'] + grp.get_group('Arkansas').max()['cases'] + grp.get_group('Colorado').max()['cases'] + grp.get_group('Kansas').max()['cases']
bordering_Oregon = grp.get_group('Nevada').max()['cases'] + grp.get_group('Washington').max()['cases'] + grp.get_group('California').max()['cases'] + grp.get_group('Idaho').max()['cases']
bordering_Pennsylvania = grp.get_group('New York').max()['cases'] + grp.get_group('Ohio').max()['cases'] + grp.get_group('West Virginia').max()['cases'] + grp.get_group('Delaware').max()['cases'] + grp.get_group('New Jersey').max()['cases'] + grp.get_group('Maryland').max()['cases']
bordering_RhodeIsland = grp.get_group('Massachusetts').max()['cases'] + grp.get_group('New York').max()['cases'] + grp.get_group('Connecticut').max()['cases']
bordering_SouthCarolina = grp.get_group('North Carolina').max()['cases'] + grp.get_group('Georgia').max()['cases']
bordering_SouthDakota = grp.get_group('Nebraska').max()['cases'] + grp.get_group('North Dakota').max()['cases'] + grp.get_group('Wyoming').max()['cases'] + grp.get_group('Iowa').max()['cases'] + grp.get_group('Minnesota').max()['cases'] + grp.get_group('Montana').max()['cases']
bordering_Tennessee = grp.get_group('Mississippi').max()['cases'] + grp.get_group('Missouri').max()['cases'] + grp.get_group('North Carolina').max()['cases'] + grp.get_group('Virginia').max()['cases'] + grp.get_group('Alabama').max()['cases'] + grp.get_group('Arkansas').max()['cases'] + grp.get_group('Georgia').max()['cases'] + grp.get_group('Kentucky').max()['cases']
bordering_Texas = grp.get_group('New Mexico').max()['cases'] + grp.get_group('Oklahoma').max()['cases'] + grp.get_group('Arkansas').max()['cases'] + grp.get_group('Louisiana').max()['cases']
bordering_Utah = grp.get_group('Nevada').max()['cases'] + grp.get_group('New Mexico').max()['cases'] + grp.get_group('Wyoming').max()['cases'] + grp.get_group('Arizona').max()['cases'] + grp.get_group('Colorado').max()['cases'] + grp.get_group('Idaho').max()['cases']
bordering_Vermont = grp.get_group('New Hampshire').max()['cases'] + grp.get_group('New York').max()['cases'] + grp.get_group('Massachusetts').max()['cases']
bordering_Virginia = grp.get_group('North Carolina').max()['cases'] + grp.get_group('Tennessee').max()['cases'] + grp.get_group('West Virginia').max()['cases'] + grp.get_group('Kentucky').max()['cases'] + grp.get_group('Maryland').max()['cases']
bordering_Washington = grp.get_group('Oregon').max()['cases'] + grp.get_group('Idaho').max()['cases']
bordering_WestVirginia = grp.get_group('Pennsylvania').max()['cases'] + grp.get_group('Virginia').max()['cases'] + grp.get_group('Kentucky').max()['cases'] + grp.get_group('Maryland').max()['cases'] + grp.get_group('Ohio').max()['cases']
bordering_Wisconsin = grp.get_group('Michigan').max()['cases'] + grp.get_group('Minnesota').max()['cases'] + grp.get_group('Illinois').max()['cases'] + grp.get_group('Iowa').max()['cases']
bordering_Wyoming = grp.get_group('Nebraska').max()['cases'] + grp.get_group('South Dakota').max()['cases'] + grp.get_group('Utah').max()['cases'] + grp.get_group('Colorado').max()['cases'] + grp.get_group('Idaho').max()['cases'] + grp.get_group('Montana').max()['cases']


###############################################################################
#creates a second graph with all the bordering states data
###############################################################################
border = {'Border State': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'],
            'Total Cases': [bordering_alabama, bordering_alaska, bordering_arizona, bordering_Arkansas, bordering_California, bordering_Colorado, bordering_Connecticut, bordering_Delaware, bordering_florida, bordering_Georgia, bordering_Hawaii, bordering_Idaho, bordering_Illinois, bordering_Indiana, bordering_Iowa, bordering_Kansas, bordering_Kentucky, bordering_Louisiana, bordering_Maine, bordering_Maryland, bordering_Massachusetts, bordering_Michigan, bordering_Minnesota, bordering_Mississippi, bordering_Missouri, bordering_Montana, bordering_Nebraska, bordering_Nevada, bordering_NewHampshire, bordering_NewJersey, bordering_NewMexico, bordering_NewYork, bordering_NorthCarolina, bordering_NorthDakota, bordering_Ohio, bordering_Oklahoma, bordering_Oregon, bordering_Pennsylvania, bordering_RhodeIsland, bordering_SouthCarolina, bordering_SouthDakota, bordering_Tennessee, bordering_Texas, bordering_Utah, bordering_Vermont, bordering_Virginia, bordering_Washington, bordering_WestVirginia, bordering_Wisconsin, bordering_Wyoming]}
border_df = pd.DataFrame(border)
border_df.plot.bar(x="Border State", y="Total Cases", title="Bordering States Total Number of COVID19 Cases");
plt.show(block=True)

# #this is a test print to make sure the code is working for bordering states
# print ("Total cases for Florida, Alabama and Georgia is: ", bordering_florida)
