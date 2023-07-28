import requests

url = "https://download.scdn.co/SpotifySetup.exe"

response = requests.get(url)

with open('SpotifySetup.exe', 'wb') as f:
    f.write(response.content)
   