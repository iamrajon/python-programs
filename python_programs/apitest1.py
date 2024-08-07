
import requests

URL = "http://127.0.0.1:8000/student_api/3/"

request = requests.get(url=URL)

data = request.json()
print(f"data from api:{data}")