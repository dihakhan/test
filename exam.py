import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter location: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1791841.xml"
print('Retrieving', url)
    
data = urllib.request.urlopen(url).read()

print('Retrieved', str(len(data)), 'characters')
    
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print("Count:",str(len(counts)))
som=0
for n in counts:
    
    som=som+int(n.text)
        #print("Add",som)
print("sum",str(som))