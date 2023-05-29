import requests

url = "http://localhost:5000/predict_api"
r = requests.post(url, json={'cgpa': 8, 'iq': 90})

print(r.json)
