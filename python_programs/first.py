
import json
#
# python_data = {'name':'Rajon', 'roll':18, 'city':'Tandi'}
#
# json_data = json.dumps(python_data)
#
# print(json_data)


json_data = {
    "name": "Rajon Chaudhary",
    "roll": 18,
    "city": "Tandi"
}
json_string = json.dumps(json_data)
# print(json_string)
python_data = json.loads(json_string)

print(python_data)

