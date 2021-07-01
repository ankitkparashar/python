import requests

api_key = "f51f4b719a401b28a3300b1ac96ac2df"
lat = 28.632429
lon = 77.218788

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

API_URL = f"https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(url=API_URL, params=weather_params)
response.raise_for_status()
weather_data: object = response.json()
# print(weather_data["hourly"])
will_rain = False

for hour in weather_data["hourly"]:
    if hour["weather"][0]["id"] < 700:
        will_rain = True
        break
