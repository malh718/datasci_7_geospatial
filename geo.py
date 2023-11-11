import requests
import urllib.parse
import json
import geopandas as gpd
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

list_of_address = pd.read_csv("slim.csv",nrows=100)
list_of_address
google_response = []

api_key = os.getenv("GOOGLE_MAPS_API")
for address in list_of_address: 
    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    print(f'....finished with {address}')


df2 = pd.DataFrame(google_response)
df2.to_csv('geo.csv')