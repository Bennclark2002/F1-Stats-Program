import requests

response = requests.get("http://ergast.com/api/f1/drivers?=123")

print(response.status_code)
