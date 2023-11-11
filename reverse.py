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

api_key = os.getenv("GOOGLE_MAPS_API")

df_cc = pd.read_csv("cc.csv")
df_cc['GEO'] = df_cc['X'].astype(str) + ',' + df_cc['Y'].astype(str)
df_cc_sample = df_cc.sample(100)

google_response = []

for coordinates in df_cc_sample['GEO']: 

 search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

 location_raw = coordinates
 location_clean = urllib.parse.quote(location_raw)

 url_request_part2 = search + location_clean + '&key=' +api_key
 url_request_part2

 response = requests.get(url_request_part2)
 response_dictionary = response.json()

 address = response_dictionary['results'][0]['formatted_address']

 final = {'address': address, 'coordinates': coordinates}
 google_response.append(final)

 print(f'....finished with {coordinates}')

df_c = pd.DataFrame(google_response)
df_c.to_csv('reverse_geo.csv')