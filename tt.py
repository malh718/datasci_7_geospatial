import requests
import pandas as pd
import urllib.parse
import os

api_key = "AIzaSyCI4TXTYXT5GOHEZnwj1lnOniYj3iywvQs"

# Load the addresses and coordinates datasets
addresses_df = pd.read_csv("slim.csv")
coordinates_df = pd.read_csv("assignment7_slim_hospital_coordinates.csv")

# Randomly select 100 rows from each dataset
sampled_addresses = addresses_df.sample(n=100, random_state=42)
sampled_coordinates = coordinates_df.sample(n=100, random_state=42)

# Initialize lists to store geocoding and reverse geocoding results
geocoding_results = []
reverse_geocoding_results = []

for address in df_sample['GEO']: 
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

    print(f'.finished with {address}')
# Create DataFrames from the results
geocoding_df = pd.DataFrame(geocoding_results)
reverse_geocoding_df = pd.DataFrame(reverse_geocoding_results)

# Save the results to CSV files
geocoding_df.to_csv('geocoding_results.csv', index=False)
reverse_geocoding_df.to_csv('reverse_geocoding_results.csv', index=False)

print("Geocoding and reverse geocoding completed.")