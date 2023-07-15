import requests
from datetime import datetime
MY_LAT = 30.748882
MY_LNG = 76.641357

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# # print(longitude, latitude)

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0   
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)
