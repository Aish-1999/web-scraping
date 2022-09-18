#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.gartner.com/en/newsroom/press-releases/2018-01-11-gartner-says-worldwide-pc-shipments-declined-2-percent-in-4q17-and-28-percent-for-the-year'

page = requests.get(url)
page

soup = BeautifulSoup(page.text , 'lxml')
soup

table = soup.find('table') #getting the first table
table


# In[2]:


table2 = table.find_all('td', {'valign': 'top'}) #getting the headings all [td-one cell so i tell get me all cells whose valign is top]
table2


# In[3]:


head = []

for i in table2:
    title = i.text
    head.append(title)

#after having the headers we should create a data frame 

ds = pd.DataFrame(columns =  head)

table3 = table.find_all('tr')[1:] #from the first table find all the row tags
table3#


# In[9]:


for j in table3:
     row = j.find_all('td')
     print(row) #to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1
     print(row1)


# In[ ]:





# In[13]:


ds.to_csv('/Users/aishwaryas/Desktop/python web scarpaing/table_scraped2.csv')


# In[ ]:




