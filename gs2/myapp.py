import requests 
import json
# url from which we need to request the data
URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name' : 'Simran',
    'roll' : 106,
    'city' : 'Goa',
}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)