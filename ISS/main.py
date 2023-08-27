import requests
from datetime import datetime

MY_LAT = 50.064651
MY_LONG = 19.944981

# GETTING position of ISS

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data= response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])

is_near = False
if MY_LAT < iss_lat +5 and MY_LAT > iss_lat -5 and MY_LONG < iss_long +5 and MY_LONG > iss_long -5:
    is_near = True

print((iss_lat,iss_long))
print(is_near)





parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0

}
response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sr_h = int(sunrise.split("T")[1].split(":")[0])
ss_h = int(sunset.split("T")[1].split(":")[0])

h = datetime.now().hour

print(h not in range(sr_h,ss_h))


if is_near ==True and h not in range(sr_h,ss_h):
    print("Check the sky!")
else:
    print("No point in going out!")