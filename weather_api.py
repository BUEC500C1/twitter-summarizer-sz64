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
	w_r = requests.get('https://api.weather.gov/points/39.7456,-97.0892');
	if str(w_r) == '<Response [200]>':
		w_d = json.loads(w_r.text)
		cwa = w_d['properties']['cwa'];
		gridx = w_d['properties']['gridX'];
		gridy = w_d['properties']['gridY'];
		w_r2 = requests.get('https://api.weather.gov/gridpoints/TOP/31,80/forecast?units=us');
		if str(w_r2) == '<Response [200]>':
			w_d2 = json.loads(w_r2.text)
			Temp = w_d2['properties']['periods'][period]['temperature'];
	return Temp;