from datetime import datetime

import requests

USERNAME = "ankitkp"
TOKEN = "uishuouieyhfkhjb"
GRAPHID = "graph1"

pixela_end_point = "https://pixe.la/v1/users"
graph_end_point = f"{pixela_end_point}/{USERNAME}/graphs"
graph_data_end_point = f"{graph_end_point}/{GRAPHID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notminor": "yes"
}

graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_data = {
    #    "date": datetime.today().strftime("%Y%m%d"),
    "quantity": "4",

}

# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.text)

# response = requests.post(url=graph_end_point, json=graph_config, headers=headers)
# print(response.text)

# response = requests.post(url=graph_data_end_point, json=graph_data, headers=headers)
# print(response.text)

response = requests.delete(url=f'{graph_data_end_point}/{datetime.today().strftime("%Y%m%d")}', headers=headers)
print(response.text)
