import requests
from datetime import datetime


USERNAME = "aweya"
TOKEN = "fgv34hnagvehr56"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {"token":TOKEN, "username": USERNAME,
               "agreeTermsOfService": "yes", "notMinor": "yes"}
# response= requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint =f"https://pixe.la/v1/users/{USERNAME}/graphs"
# graph_configuration = { "id": "graph1", "name": "FC 25 graph",
#                        "unit": "minute","type": "float","color": "ajisai"}
headers = {"X-USER-TOKEN": TOKEN}
# response =requests.post(url=graph_endpoint, json=graph_configuration, headers= headers)
# print(response.text)
today = datetime.now()
pixel_configuration = { "id": "graph1", "date": today.strftime("%Y%m%d"),
                       "quantity": input("How many minutes did you play today? ")}
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"
response = requests.post(url=pixel_endpoint, json=pixel_configuration, headers=headers)
# print(response.text)
# update_pixel_config = {"quantity": "50"}
# update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/20250901"
# # response= requests.put(url=update_pixel_endpoint, json=update_pixel_config,headers=headers)
# print(response.text)

# delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/20250901"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)