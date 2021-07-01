import requests

parameters = {
    "lat": 28.632429,
    "lng": 77.218788,
    "formatted": 0
}
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()["iss_position"]

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
print(response.json())
