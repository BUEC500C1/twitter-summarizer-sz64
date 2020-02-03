import weather_api as w

def test_valid():
	assert ('140.386001587', '35.7647018433') == w.get_coord("Narita International AiRport");
