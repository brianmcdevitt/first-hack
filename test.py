from urllib.request import urlopen
import json
from twilio.rest import TwilioRestClient

credentials = open()

google_api = "http://maps.googleapis.com/maps/api/geocode/json?address="
weather_api = "http://api.openweathermap.org/data/2.5/weather?q="

def find_weather(zip_code):
	response = urlopen(google_api + str(zip_code)).read().decode('utf8')
	json_response = json.loads(response)
	city_name = json_response["results"][0]["formatted_address"]
	response = urlopen(weather_api + city_name.replace(' ', '%20')).read().decode('utf8')
	json_response = json.loads(response)

	weather = json_respnse["weather"][0]

	weather_des = weather["main"] + " | " + weather["description"]

	message = 


	print(city_name)

find_weather("07869")