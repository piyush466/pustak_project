import requests


request = requests.get("https://reqres.in/api/users?page=2")
print(request.status_code)
print(request.json())
assert  request.status_code == 200

# requests.post("")