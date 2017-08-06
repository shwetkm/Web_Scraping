# -*- coding: utf-8 -*-

#import the library used to query a website
import urllib2
#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "lxml")

right_table=soup.find_all('table', class_='wikitable sortable')

A=[]
B=[]
C=[]

for i in range(0,len(right_table)):
    for row in right_table[i].findAll("tr"):
        cells = row.findAll('td')
        if len(cells)==5 or len(cells)==6: #Only extract table body not heading
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[4].find(text=True))

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['City']=B
df['State/UT']=C

def City(state):
    try:
        ct = df[df['State/UT'] == state].City.values
        print ct[0], ct[1]
    except:
        print('Please enter a valid State !')
    
x = raw_input("Enter state name: ")

City(x)