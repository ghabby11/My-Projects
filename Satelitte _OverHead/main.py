import requests
from datetime import datetime
import  smtplib
import time


MY_LAT = 5.603717 # Your latitude
MY_LONG = -0.186964 # Your longitude
my_email = "gabpythontest@gmail.com"
password = "gdlooyovxustfoyl"




#Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # If the ISS is close to my current position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    if sunset <= hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs="gabrielacehood@yahoo.com",
                                    msg=f"Subject:ISS Position\n\n Look ⬆️ to see the ISS")

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



