"""
curl -X POST -H "Content-type: application/json" -d \
'{"name": "catty mcCatFace", "price": 5000, "breed": "bengal"}' \
'http://127.0.0.1:5000/add'
"""

import requests


url = "http://127.0.0.1"
port = 5000

def add_dummy_data():

    data = [["a", 200, "b"],
            ["c", 400, "d"],
            ["e", 600, "f"],
            ["g", 800, "h"],
            ["i", 1000, "j"]]

    for name, price, breed in data:
        payload = {"name": name, "price": price, "breed": breed}
        response = requests.post(f"{url}:{port}/add", json=payload)
        print(response)
        print(response.reason)


if __name__ == "__main__":
    add_dummy_data()
