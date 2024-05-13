import requests
import json

API_ENDPOINT = "http://127.0.0.1:8000/items"

request_header = {
    "Content-Type": "application/json"
}

price = 2.45
tax_rate = 0.05
tax = price * tax_rate

request_body = {
    "name": "bread",
    "description": "yummy",
    "price": price,
    "tax": tax
}

response = requests.post(
    url=API_ENDPOINT, 
    headers=request_header,
    json=request_body
)

if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Error: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
