import os
import requests
from twilio.rest import Client

params={"lat" : 5.639585,
        "lon":0.248281,
"appid":"1f245a720397aa046047ea04ee786c05",
        "cnt": 4

}

account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"


url= "https://api.openweathermap.org/data/2.5/forecast"


response = requests.get(url=url, params=params)
response.raise_for_status()
data = response.json()

weather = [forecast for  forecast in data["list"]]

will_rain = False
for d in data["list"]:
    condition_code= d["weather"][0]["id"]
    if condition_code <700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
    body="The sun will come down, dont bring an umbrella☔️",
    from_="whatsapp:+14155238886",
    to="whatsapp:+233548457026")

    print(message.status)
    # print(t)
# print(weather[])
# for i in weather:
#     if i["weather"][i]["id"] < 700:
#         print("Bring an Umbrella")
# print(weather)
# print(data["list"][0]["weather"][0]["id"])
# # print(response.status_code)}
