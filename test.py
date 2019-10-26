

import openrouteservice
from openrouteservice import convert

import os
import json
'''
install ors library:
https://openrouteservice-py.readthedocs.io/en/latest/

get your api key:
https://openrouteservice.org/dev/#/home

paste it into key.txt (keep your key to yourself!)
'''
#print(os.getcwd())

routes = []

start = (8.34234,48.23424)
end = (8.34423,48.26424)
coords = (start, end)
keyfile = open('key.txt', 'r')
key = keyfile.read()
client = openrouteservice.Client(key=key) # Specify your personal API key
# decode_polyline needs the geometry only
geometry = client.directions(coords)['routes'][0]['geometry']
routes.append(geometry)

with open('route.geojson', 'w') as outfile:
    json.dump(geometry, outfile)

decoded = convert.decode_polyline(geometry)

print(decoded)
