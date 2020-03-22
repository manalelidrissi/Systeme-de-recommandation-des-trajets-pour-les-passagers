# we wanna aggregate all datasets in one clean data set 
# columns are : 
# company         : 1-ONCF,2-CTM,3-TAXI,4-Covoiturage
# from_lat        : latitude of the origine city
# from_lan        : langitude of the origine city
# to_lat          : latitude of the destination city
# to_lan          : langitude of the destination city
# distance        : distance between origin and destination
# duration        : traveling duration
# driver_sex      : driver sex 0 if unkown(for example train...)
# driver_age      : driver age 0 if unkown
# price           : travling cost


import numpy as np
import requests
import json
from math import sin, cos, sqrt, atan2, radians
import pandas as pd


def getLocationOfCity(city):
	api_key = '966a766bb88e4cb5a5f78ffd9ec99208'
	req = requests.get('https://api.opencagedata.com/geocode/v1/json?q='+city+'&key='+api_key)
	js = json.loads(req.text)
	rep = None
	for res in js['results']:
		if res['formatted'].split(',')[-1] == " Morocco":
			rep = res['geometry'] 
			break
	return rep

def distance(locationA,locationB):
	R = 6373.0

	lat1 = radians(locationA['lat'])
	lon1 = radians(locationA['lon'])
	lat2 = radians(locationB['lat'])
	lon2 = radians(locationB['lon'])

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c
	return distance

def preprocessing(datafile):
	"""
	take a data source csv and make it respect the new format with the new columns
	"""
	df = pd.read_csv(datafile,delimiter=";")
	fromLocation = [getLocationOfCity(city) for city in df["from"]]
	toLocation = [getLocationOfCity(city) for city in df["to"]]

	print(fromLocation)

if __name__ == '__main__':
	preprocessing('OncfTrips.csv')