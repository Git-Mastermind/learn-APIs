import requests

data = {
    "name":"Eshan",
    "age":14,
    "fav_food":"palak paneer",
    "fav_vid_game":"hogwarts legacy"
}

post_request = requests.post("https://jsonplaceholder.typicode.com/posts", data)
print(post_request.status_code)