import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input("Enter:-")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
som=0
tags=soup('span')
for tag in tags:
  
    num=re.findall('[0-9]+',str(tag))
    for n in num:
        #print("eachnumb",(n))
        som=som+int(n)
        #print("Add",som)
print(som)
    