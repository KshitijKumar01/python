import requests

API_KEY = "e2aefec44068c281fc628605470fb3b1"
API = "https://api.openweathermap.org/data/3.0/onecall"
LAT = 30.733315
LNG = 76.779419

param = {
    "lat" : 30.733315,
    "lon" : 76.779419,
    "appid" : API_KEY
}

response = requests.get(API, params=param)
print(response.status_code)
data = response.json()
print(data)
