import requests

API_KEY = "AIzaSyC5xN7-YOUR-GOOGLE-KEY-HERE"
url = f"https://maps.googleapis.com/maps/api/geocode/json?address=New+York&key={API_KEY}"

response = requests.get(url)
print(response.json())
