import requests
import json
url="http://www.official-joke-api.appspot.com/random_joke"
response = requests.get(url)
data=response.json()
# print(data['setup'])
# print(data['punchline'])
dic=json.loads(response.text)
print(dic['setup'])
print(dic['punchline'])