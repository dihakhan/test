import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
   

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

#Generating the complete URL. Printing it in order to check if it's correct.
queryurl = serviceurl.strip() + url.strip()
print("DATA URL: ", queryurl)
#Obtaining and reading the data
try :
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    
    js = json.loads(data)
    
    print(js)
    place_id = js["results"][0]["place_id"]
    print("PLACE ID: ", place_id)
except:
    print("Error.....")
    print("-"*50)
    print(data)

    