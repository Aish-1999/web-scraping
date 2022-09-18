#WEB SCRAPING A WEBPAGE USING BEAUTIFULSOUP IN PYTHON
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

#scraping out the headings in a table 

table2 = table.find_all('td', {'valign': 'top'}) #getting the headings all [td-one cell so i tell get me all cells whose valign is top]
table2

tableno = table.find_all('td', {'valign': 'top'})[0] #getting the headings particular
tableno

tableno.attrs# getting the attributes of company

tableno.text# getting the text of index 0

#getting all the string of headings  and putting it in table form

head = []

for i in table2:
    title = i.text
    head.append(title)

#after having the headers we should create a data frame 

ds = pd.DataFrame(columns =  head)

table3 = table.find_all('tr')[1:] #from the first table find all the row tags
table3#it has our heading and we dont want it we index it from1 which is 2nd

for j in table3:
    row = j.find_all('td')
    break#find all the data in one row
    row
    row = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
    
 for j in table3[0:1]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1# to put the rows in dataframe

for j in table3[1:2]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1

for j in table3[2:3]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1#

for j in table3[3:4]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1#
     
 for j in table3[4:5]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1
     
 for j in table3[5:6]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1

 for j in table3[6:7]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1
     
 for j in table3[7:8]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1
     
 for j in table3[1:]:
     row = j.find_all('td')
     row#to access every value in row individually we use td
     

     row1 = [tr.text for tr in row] #it goes and takes the td tag data in that row and puts it back in the list
     length = len(ds)
     ds.loc[length] = row1
     
#export as csv file

ds.to_csv('/Users/aishwaryas/Desktop/python web scarpaing/table_scraped.csv')

#webscraping the second table hence we use indexing method to get the second table

table_=soup.find_all('table')[1]
table_
     
table2_ = table.find_all('td', {'valign': 'top'}) #getting the headings all [td-one cell so i tell get me all cells whose valign is top]
table2_

head_= []

for i in table2_:
    title = i.text
    head_.append(title)
    
ds1 = pd.DataFrame(columns =  head_)

table3_ = table_.find_all('tr')[1:] #from the first table find all the row tags
table3_

 for j in table3_[0:1]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_# to put the rows in dataframe

for j in table3_[1:2]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_

for j in table3_[2:3]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_#

for j in table3_[3:4]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_#

     
for j in table3_[4:5]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_#

     
for j in table3_[5:6]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_#


for j in table3_[6:7]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_#

for j in table3_[7:8]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_#

     
for j in table3_[1:]:
     row_ = j.find_all('td')
     row_#to access every value in row individually we use td
     

     row1_ = [tr.text for tr in row_] #it goes and takes the td tag data in that row and puts it back in the list
     length_ = len(ds1)
     ds1.loc[length_] = row1_#

     
#export as csv file

ds1.to_csv('/Users/aishwaryas/Desktop/python web scarpaing/table_scraped1.csv')

#webscraping the second table hence we use indexing method to get the second table
