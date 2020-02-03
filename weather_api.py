import json
import requests

def get_coord(airport):
	latitude = "Error";
	longitude = "Error";
	with open('airport-codes_json.json') as ap_codes:
		ap_data = json.load(ap_codes);
		for a in ap_data:
			if a['name'].lower() == airport.lower():
				coord = a['coordinates'];
				coord = coord.split(', ');
				latitude = coord[0];
				longitude = coord[1];
				break
	return latitude, longitude;
	
def get_temp(latitude, longitude, period = 0):
	Temp = "Error";
	req1 = 'https://api.weather.gov/points/' + str(longitude) + ',' + str(latitude);
	w_r = requests.get(req1);
	if str(w_r) == '<Response [200]>':
		w_d = json.loads(w_r.text)
		cwa = w_d['properties']['cwa'];
		gridx = w_d['properties']['gridX'];
		gridy = w_d['properties']['gridY'];
		req2 = 'https://api.weather.gov/gridpoints/' + cwa + '/' + str(gridy) + ',' + str(gridx) + '/forecast?units=us';
		w_r2 = requests.get(req2);
		if str(w_r2) == '<Response [200]>':
			w_d2 = json.loads(w_r2.text)
			Temp = w_d2['properties']['periods'][period]['temperature'];
	return Temp;