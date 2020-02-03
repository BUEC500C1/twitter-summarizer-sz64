import weather_api as w

def test_valid_getcoord():
	assert ('140.386001587', '35.7647018433') == w.get_coord("Narita International AiRport");
	assert ('140.386001587', '35.7647018433') == w.get_coord("NARITA INTERNATIONAL AIRPORT");
	assert ('140.386001587', '35.7647018433') == w.get_coord("narita international airport");
	
def test_invalid_getcoord():
	assert ('140.386001587', '35.7647018433') == w.get_coord("NARITA AIRPORT");
	assert ('140.386001587', '35.7647018433') == w.get_coord("NARITA INTERNATIONAL AIRPORT ");
	assert ('140.386001587', '35.7647018433') == w.get_coord("NARITA1 INTERNATIONAL AIRPORT");
	
def test_valid_temp():
	assert isinstance(w.get_temp(-95.622497558594,39.068698883057),int);
	
def test_invalid_temp():
	assert "Error" == w.get_temp('a','b');
	assert "Error" == w.get_temp('-100','-200');
	assert "Error" == w.get_temp('///','12');