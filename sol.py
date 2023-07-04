import urllib.request,urllib.parse,urllib.error
import json


address = input('Enter location: ')

print('Retrieving', address)
url=urllib.request.urlopen(address)
data=url.read().decode()#utf8 turn into unicode
js=json.loads(data)  
print('Retrieved',len(str(js)),'charachters')
    
data1 = js.get("comments")

num = total = 0
for i in range(len(data1)):
    tmp = data1[i]
    value = tmp.get("count")
    num = num + 1
    total = total + int(value)
print("Count:",num)
print("Sum:",total)