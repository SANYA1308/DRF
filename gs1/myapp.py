import requests 
# url from which we need to request the data
URL = "http://127.0.0.1:8000/stuinfo/2"

r = requests.get(url = URL)
data = r.json()
print(data)