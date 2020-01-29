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
	
def get_temp(latitude, longitude):
	Temp = "Error";
	w_r = requests.get('https://api.weather.gov/points/39.7456,-97.0892');
	w_d = json.load(w_r.text)
	return Temp;