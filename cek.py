import requests

TOKEN = "7336091968:AAFJ1rnjFJFjPb1hfBnzy7ZGcGVFB8LUijc"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)
print(response.json())
