import requests

API_KEY = "e541e211078b4b30b5253644253101"  # Replace with your WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"  # Excludes air quality index to keep it simple
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if "error" in data:
        print("City not found. Please check the name and try again.")
        return

    location = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]

    print(f"Weather in {location}, {country}: {condition}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
