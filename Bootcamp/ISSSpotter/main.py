# import pytz
import requests
from datetime import datetime
from pytz import timezone

MY_LAT = 28.632429  # Your latitude
MY_LONG = 77.218788  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_near():
    global MY_LAT, MY_LONG, iss_latitude, iss_longitude
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
# print(time_now)
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

frmt = "%Y-%m-%dT%H:%M:%S"
sunrise_hour = datetime.strptime(data["results"]["sunrise"][:19], frmt)
# print(sunrise_hour)
print(sunrise_hour.astimezone(timezone('Asia/Kolkata')))
