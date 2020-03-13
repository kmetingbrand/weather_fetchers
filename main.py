import requests
import json

key_file = open("key.txt")
key = key_file.readline()
icao = input("Input the airport code to retrieve weather data: ")
icao = icao.upper()

hdr = { 'X-API-Key': key }
req = requests.get(f'https://api.checkwx.com/metar/{icao}/decoded', headers=hdr)
response = json.loads(req.text)
print(response)

if response['results'] == 1:
    print("hooray you have a response")
    wind_degrees = response['data'][0]['wind']['degrees']
    airport_name = response['data'][0]['station']['name']
    wind_speed_kts = response['data'][0]['wind']['speed_kts']
    temperature = response['data'][0]['temperature']['celsius']
    humidity = response['data'][0]['humidity']['percent']
    barometer = response['data'][0]['barometer']['hpa']
    visibility_miles = response['data'][0]['visibility']['miles']
    visibility_meters = response['data'][0]['visibility']['meters']
    elevation = response['data'][0]['elevation']['meters']
    clouds_dict = response['data'][0]['clouds']
    my_clouds = []
    if len(clouds_dict) > 0:
        for c in clouds_dict:
            clouds = c['text']
            my_clouds.append(clouds)
    else:
        my_clouds.append("No clouds")
    conditions_dict = response['data'][0]['conditions']
    if len(conditions_dict) > 0:
        conditions = response['data'][0]['conditions'][0]['text']
    else:
        conditions = "none"
    flight_category = response['data'][0]['flight_category']
    print(f"The current wind degrees in {airport_name} is {wind_degrees} at {wind_speed_kts} kts.\n")
    print(f"The temperature at {airport_name} is {temperature} degrees Celsius at humidity of {humidity} percent.\n")
    print(f"The air pressure is at {barometer} hPa.\n")
    print(f"Current visibility extends to {visibility_miles} in miles or {visibility_meters} in meters.\n")
    print(f"Elevation of the airport is {elevation} meters.")
    print(f"The current weather conditions are the following: {conditions}.\n")
    print(f"Current clouds are: {', '.join(my_clouds)}.\n")
    print(f"The flight category is {flight_category}")
else:
    print("incorrect code")
