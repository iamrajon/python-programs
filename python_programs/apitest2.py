import json
import requests


URL = "http://127.0.0.1:8000/create_student/"

data = {
    'name': 'Baverly Marsh',
    'roll': 17,
    'city': 'Derry'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

json_res = r.json()
print(json_res)

