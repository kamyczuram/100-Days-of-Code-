import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "cutlocus"
TOKEN = "PRIVATE!"

user_params ={
    "token": "zzzzzpa245Gp8",
    "username": "cutlocus",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "pierwszygraf",
    "name": "Programowanko",
    "unit": "min",
    "type": "int",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN

}
# response = requests.post(url=graph_endpoint, json= graph_config, headers=headers)
# print(response.text)

progress_config ={
    "date": "20230829",
    "quantity": "180"

}

# response = requests.post(url=f"{graph_endpoint}/pierwszygraf", json=progress_config, headers=headers)
# print(response.text)
print(datetime.datetime.now().strftime("%Y%m%d"))

