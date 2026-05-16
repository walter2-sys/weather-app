import requests
import json 
from datetime import datetime
import os

api_key = os.getenv("WEATHER_API_KEY")
if not api_key:
       print("Error: WEATHER_API_KEY not set.")
       exit()
       
base_url = f"https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
        try: 
              url = f"{base_url}?q={city}&appid={api_key}&units=metric"
              response = requests.get(url)
              data = response.json()

              if data.get("cod") == 200:
                     return data
              else:
                     print("City not found. Try again")
                     return None
        except requests.exceptions.RequestException:
              print("Network Error. Try again.")
              return None
        
def get_emoji(description):
       if "clear" in description:
              return "☀"
       elif "rain" in description:
              return "🌧"
       elif "snow" in description:
              return "❄"
       elif "cloud" in description:
              return "☁"
       else: 
              return "🌈"
       
def get_temp_emoji(temp):
       if temp <= 0:
              return "🥶"
       elif temp <= 10:
              return "🧥"
       elif temp <= 20:
              return "🙂"
       elif temp <= 30:
              return "😎"
       else:
              return "🔥"

while True:
        city = input("Enter city or exit: ")
        if city.lower() == "exit":
                break 
        data = get_weather(city)

        if data:
              # print(json.dumps(data, indent=4))
               temp = data["main"]["temp"]
               temperature = get_temp_emoji(temp)
               description = data["weather"][0]["description"].lower()
               emoji = get_emoji(description)
               humidity = data["main"]["humidity"]
               fl = data["main"]["feels_like"]
               pressure = data["main"]["pressure"]
               wind_speed = data["wind"]["speed"]
               country = data["sys"]["country"]
               sunrise = data["sys"]["sunrise"]
               sunset = data["sys"]["sunset"]
               sunrise_time = datetime.fromtimestamp(sunrise)
               sunset_time = datetime.fromtimestamp(sunset)
               
               print("\nWeather Report")
               print("------------------")
               print(f"Weather in {city}, {country}")
               print(f"Temperature {temp}°C{temperature}")
               print(f"humidity: {humidity}%")
               print(f"Feels like: {fl}")
               print(f"{emoji}Description: {description}")
               print(f"Pressure: {pressure}")
               print(f"Wind Speed: {wind_speed} m/s")
               print(f"Sunrise:", sunrise_time.strftime("%H:%M"))
               print(f"Sunset: ", sunset_time.strftime("%H:%M"))