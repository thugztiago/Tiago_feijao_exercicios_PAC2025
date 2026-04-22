import requests as re

response=re.post("http://localhost:2525/docs/gettingStarted")
print(response.text)