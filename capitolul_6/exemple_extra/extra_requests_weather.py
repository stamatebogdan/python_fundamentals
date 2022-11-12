import json
import requests

url_locatie = "https://www.metaweather.com/api/location/search/?lattlong=44.42,26.10"

response = requests.get(url_locatie)

json_data = json.loads(response.text)

print(json_data)

for oras in json_data:
    if oras["title"] == "Bucharest":
        woeid = oras['woeid']
        break

url_vreme="https://www.metaweather.com/api/location/" + str(woeid)

response=requests.get(url_vreme)
json_vreme= response.json()

print(json_vreme)

for zi in json_vreme["consolidated weather"]:
    print("Vremea pentru ziua " + zi["applicable_date"])
    print("Temperatura maxima %f" % zi["max_temp"])
    print("Temperatura minima %f" % zi["min_temp"])
    print("Presiunea aerului %f" % zi["air_pressure"])
    print("Umiditatea %d" % zi["humidity"])
    print("Viteza vantului %f" % zi["wind_speed"])