#web scraping airbnb every single hotel detail therefore working on multiple webpage scraping
import requests
from bs4 import BeautifulSoup
import pandas as pd


url='https://www.airbnb.co.in/s/Europe/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&place_id=ChIJhdqtz4aI7UYRefD8s-aZ73I&date_picker_type=calendar&checkin=2022-09-30&checkout=2022-10-30&source=structured_search_input_header&search_type=filter_change&query=Europe&price_filter_num_nights=30&federated_search_session_id=4d03e6a8-778f-4d74-bc88-0f09b6d7ac40&pagination_search=true'
page = requests.get(url)
page

soup = BeautifulSoup(page.text , 'lxml')
soup

#wanting those a tag url which takes us to the next page only meawhile a tag with  previous also is there with same atttribute hence we need to specify


next_page = soup.find('a' , {'aria-label' : 'Next'}).get('href')# this is the url we get for next page
next_page #this gives the ouput of the link that takes us to next page but then that link when placed in the browser won't give us that web page
#hence we need to use the url in the start and combine it with this
next_page_full = 'https://www.airbnb.co.in/'+next_page
next_page_full

 #html of page 2 we got

url = next_page_full 
page = requests.get(url)
page

soup = BeautifulSoup(page.text , 'lxml')
soup
df = pd.DataFrame({'Links':[''],'Title':[''],'Price':[''],'Rating':[''],'Type':[''],'Beds':[''] })
#first using while loop we get all the postings from all the webpages it will loop till the last webpage and the give an error
while True:
    
    posting = soup.find_all('div', class_='c4mnd7m dir dir-ltr')
    for post in posting:
        try:
            link = post.find('a', {'class' : 'ln2bl2p dir dir-ltr'}).get('href')
            link_full = 'https://www.airbnb.co.in/'+link
            link_full
            title = post.find('div', {'class' : 'g1tup9az cb4nyux dir dir-ltr'})
            title
            title1=post.find('div', class_='t1jojoys dir dir-ltr')
            title_store = title1.text
            title_store
            price=post.find('span' , class_='_14y1gc').text
            price        
            rating = post.find('span', class_='ru0q88m dir dir-ltr').text
            rating
            type_ = post.find('span', class_='tjbvqj3 dir dir-ltr').text
            type_
            beds = post.find('span', class_='dir dir-ltr').text
            beds
            df = df.append({'Links':link_full,'Title':title_store,'Price':price,'Rating':rating,
                        'Type':type_,'Beds':beds} , ignore_index = True)
        except:
            pass
        #we use try and expect so that in case any data is missing it should stop searching others so any data is missing it wont print that whole posting itself
    
        
    next_page = soup.find('a' , {'aria-label' : 'Next'}) #this becomes false only when the last page has been reached and then gives an error
    next_page['href']
    next_page_full = 'https://www.airbnb.co.in/'+next_page
    next_page_full
    url = next_page_full 
    page = requests.get(url)
    page

    soup = BeautifulSoup(page.text , 'lxml')
    soup

df.to_csv('/Users/aishwaryas/Desktop/python web scarpaing/project2download.csv')
