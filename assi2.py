
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
numlist=list()
url=input("Enter:-")
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
numlist=list()
for l in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    numlist.append(tags[position].contents[0])
    html=urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(numlist[-1])