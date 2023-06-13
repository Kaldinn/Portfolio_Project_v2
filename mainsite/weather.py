from dotenv import load_dotenv
import requests


weather_api_key = "9a3b5a85fcb8310bffa11668bfb4eaf7"

weather_icons = {
    'clear sky': 'sun.png',
    'few clouds': 'cloudy.png',
    'scattered clouds': 'scatterd.png',
    'broken clouds': 'broken.png',
    'shower rain': 'shower.png',
    'rain': 'rain.png',
    'thunderstorm': 'storm.png',
    'snow': 'snow.png',
    'mist': 'mist.png',
    'overcast clouds': 'cloudy.png',
    'light rain': 'rain.png'
}

def get_weather(city_name):
    if not city_name:
        return "Enter the city name"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        icon = weather_icons.get(description, 'default.png')
        return {
            'temperature': f"Temperature in {city_name}: <h1><strong>{temperature}°C</strong></h1>",
            'description': f"Weather description: <h2><strong>{description}</h2></strong>",
            'icon': icon
        }
    else:
        return f"Error: {data['message']}"
