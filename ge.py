import requests
import pandas as pd
import re
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_MAPS_API")

list_of_address = pd.read_csv("slim.csv")
list_of_address['GEO'] = list_of_address['ADDRESS'] + ' ' + list_of_address['CITY'] + ' ' + list_of_address['STATE']
list_of_address_sample = list_of_address.sample(100)

google_response = []

for address in list_of_address_sample['GEO']:
    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    location_raw = address
    location_clean = urllib.parse.quote(location_raw)
    url_request_part1 = search + location_clean + '&key=' + api_key

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    if 'results' in response_dictionary and response_dictionary['results']:
        lat_long = response_dictionary['results'][0]['geometry']['location']
        lat_response = lat_long['lat']
        lng_response = lat_long['lng']
        final = {'address': address, 'lat': lat_response, 'lon': lng_response}
        google_response.append(final)
        print(f'Finished with {address}')
    else:
        print(f'No results for {address}')

dfnew2 = pd.DataFrame(google_response)
dfnew2.to_csv('ge.csv')