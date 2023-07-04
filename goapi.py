import urllib.request,urllib.parse,urllib.error
import json
#data pulled out of the internet

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'
#loop
while True:
    address=input('enter LocatioN ')
    if len(address)<1:break
    #concate serviceurl urlcode
    url=serviceurl+urllib.parse.urlencode(
        {'address':address})#gives use string
    #urrlib eats the headers
    print('Retr',url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()#utf8 turn into unicode
    print('retr',len(data),'charachters')
    
    try:
        js=json.loads(data)
    except:
        js=None
    
    #if we got nothing or the status key is not equal to ok
    #status can be a problem {{}} its a dictionary
    if not js or'status' not in js or js['status'] != 'OK':
        print("fail")
        print(data)
        continue
        #dumps opposite of load
    print(json.dumps(js,indent=4))
    
    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lnf',lng)
    location=js['results'][0]['formatted_address']
print(location)