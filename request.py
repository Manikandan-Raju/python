import requests

url = "https://www.python.org/static/img/python-logo@2x.png"
# query_parameters = {"downloadformat": "png"}

response = requests.get(url)

with open("python.png", mode="wb") as file:
    file.write(response.content)

import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
r = response.json()
print(r)