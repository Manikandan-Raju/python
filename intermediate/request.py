import requests
from pprint import pprint

def github_data():
    # github username
    username = "Manikandan-Raju"
    # url to request
    url = f"https://api.github.com/users/{username}"
    # make the request and return the json
    user_data = requests.get(url).json()
    # pretty print JSON data
    pprint(user_data)

def python_logo():
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
    
if __name__ == "__main__":
    github_data()
    python_logo()