import requests

url = "https://sofascore.p.rapidapi.com/tvchannels/get-available-countries"

querystring = {"matchId":"13157877"}

headers = {"Content-Type": "application/json"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())