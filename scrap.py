import pandas as pd 
from bs4 import  BeautifulSoup
import requests as rt

# HTTP Request 
website='https://www.officeholidays.com/countries/india/2022'
response= rt.get(website).text
## checking for status code 
response
## soup  object s
soup= BeautifulSoup(response,'html.parser') 
results=soup.find("table",{'class':'country-table'}).find('tbody').find_all('tr')
print(len(results))
#print(results)


# day
w=results[0].find('td').get_text().strip()
# date
e=results[0].find('td',{'style':'white-space:nowrap;'}).get_text().strip()
#comment
t=results[0].find('td',{'class':'hide-ipadmobile'}).get_text().strip()
r=results[0].find('a',{'class':'country-listing'}).get_text().strip()
#r=results[0].find('td',{'a'}).get_text().strip()


day= []
date= []
comment= []
data= []

#website
for result in results:
        #day
    try:
        day.append(result.find('td').get_text().strip())
    except:
        day.append('n/a')
        #date
    try:
        date.append(result.find('td',{'style':'white-space:nowrap;'}).get_text().strip())
    except:
        date.append('n/a')

        #comment
    try:
        comment.append(result.find('td',{'class':'hide-ipadmobile'}).get_text().strip())
    except:
        comment.append('n/a')

        #change_24h
    try:
        data.append(result.find('a',{'class':'country-listing'}).get_text().strip())
    except:
        data.append('n/a')


holiday_df=pd.DataFrame({'day':day ,'date':date, "comment":comment, "data":data})
print((holiday_df))

# converting into json
js = holiday_df.to_json("holidays days",orient="records")
print(js)
        




