import requests

data_request = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = data_request.json()

print(data)
print(data_request.status_code)