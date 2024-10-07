# Practising reading JSON from the internet
#Author: Aoife Flavin

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(f"the current price in euros is {data['bpi']['EUR']['rate_float']}")