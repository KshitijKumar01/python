import requests
from datetime import datetime
import smtplib


MY_LAT = 30.733315 # Your latitude
MY_LONG = 76.779419 # Your longitude
my_email = "ridebrave3801@gmail.com"
password = "Ridebrave*123"
generated_pass = "wwgzgpwtxxduwfiy"
to_email = "kshitijkumar.kk.sunny@gmail.com"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, generated_pass)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg="Subject:Look up\n\nThe ISS is above in the sky."
    )