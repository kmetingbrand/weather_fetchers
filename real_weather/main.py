import json
import requests

key_file = open("key.txt")
key = key_file.readline()

def weather_generator(response):
    description = response['weather'][0]['description']
    temperature = float(response['main']['temp'])
    temperature_feel = float(response['main']['feels_like'])
    temperature_min = float(response['main']['temp_min'])
    temperature_max = float(response['main']['temp_max'])
    humidity = response['main']['humidity']
    wind = response['wind']['speed']

    celsius_temp = temperature - 273
    celsius_feel = temperature_feel - 273
    celsius_min = temperature_min - 273
    celsius_max = temperature_max - 273

    weather_information = []
    latitude = response['coord']['lat']
    longitude = response['coord']['lon']

    weather_information.append(f"The weather for {city} is currently as follows: {main_info}; more precisely: {description}\n")
    weather_information.append(f"The temperature is {round(celsius_temp, 2)} C, which feels like {round(celsius_feel, 2)} C.\n")
    weather_information.append(f"The minimum temperature today is {round(celsius_min, 2)} C, with the max being {round(celsius_max, 2)} C.\n")
    weather_information.append(f"The humidity in {city} is {humidity}%. Wind is at the speed of {wind} m/s.")
    return weather_information, latitude, longitude

def weather_uv(response_uv):
    uv_level = response_uv['value']

    uv_information = f"The UV index in {city} is {uv_level}."
    return uv_information


working = True

while working == True:
    city = input("Please input the city for which you would like to view the current weather information for: ")
    req1 = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}')
    response_weather = json.loads(req1.text)
    if int(response_weather['cod']) == 200:
        result, latitude, longitude = weather_generator(response_weather)
        req2 = requests.get(f"http://api.openweathermap.org/data/2.5/uvi?appid={key}&lat={latitude}&lon={longitude}")
        response_uv = json.loads(req2.text)
        result2 = weather_uv(response_uv)
        for i in result:
            print(i)
        print(result2)
        working = False
    else:
        print("The city is either unavailable or does not exist. Try again!")