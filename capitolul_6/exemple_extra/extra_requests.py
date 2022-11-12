import requests

url="https://api.exchangerate-api.com/v4/lates/"

monede = ["USD", "EUR"]

for moneda in monede:
    response = requests.get(url + moneda)
    json_date = response.json()
    print(json_date)
    print("Cursul " + moneda + " este %f " %json_date["rates"]["RON"])

