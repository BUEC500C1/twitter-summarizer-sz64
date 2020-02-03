import weather_api as w

def example_func():
	valid_input = 1;
	while(valid_input):
		ap = input("Please enter an airport name here: "); # Example: Philip Billard Municipal Airport;
		[latitude, longitude] = w.get_coord(ap);
		if ((latitude != "Error") & (longitude != "Error")):
			valid_input = 0;
	print(w.get_temp(latitude, longitude));
	
example_func();