# Include the current weather into your game mechanics.

URL = "https://www.metaweather.com/api/"

import requests

def get_location_woeid(location):
    url = f"https://www.metaweather.com/api/location/search/?query={location}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['woeid']
        else:
            return None
    else:
        return None

def get_current_weather(woeid):
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['consolidated_weather'][0]
        return weather['weather_state_name'], weather['the_temp']
    else:
        return None, None
