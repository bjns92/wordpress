import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.flipkart.com/search?q=iphone%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
c = r.content
soup = BeautifulSoup(c,'html.parser')
all = soup.find_all('div',{'class':'_3O0U0u'})
print(len(all))

"""Deleting the item since it was having inappropriate data."""
del(all[12])

l = []
for item in all:
    d = {}
    l1 = []
    d['Name']=item.find('div',{'class':'_3wU53n'}).text
    d['Price']=item.find('div',{'class':'_1vC4OE _2rQ-NK'}).text
    d['Rating']=item.find('div',{'class':'hGSR34'}).text
    l1 = item.find('div',{'class':'_3ULzGw'}).text.split('|') 
    d['Storage'] = l1[0].strip()
    d['Display'] = l1[1][0:20].strip()
    d['Rear_Camera'] = l1[1].split('Display')[1].split(' ')[0]
    d['Front_Camera'] = l1[2].split(' ')[1]
    l.append(d)
    
print(l)

df = pd.DataFrame(l)
df.to_csv('iPhone.csv')