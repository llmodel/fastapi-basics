import requests
from dotenv import load_dotenv
import os
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

load_dotenv()
TOKEN = os.getenv("PIXELA_TOKEN")
USER_NAME = os.getenv("PIXELA_USER_NAME")

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_id = "graph1"
ADD_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{graph_id}/"

request_header = {
    "X-USER-TOKEN": TOKEN
}

# date = "20240117"
today = dt.datetime.now().strftime("%Y%m%d")
miles_walked = "5.5"

# Add a pixel to the graph
request_body = {
    "date": today,
    "quantity": miles_walked
}
response = requests.post(
    url=ADD_PIXEL_ENDPOINT, 
    headers=request_header, 
    json=request_body
)

print(response.text)
# 
# New graph link: https://pixe.la/v1/users/llgm759/graphs/graph1.html
