import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "New Post",
    "body": "This is a new post.",
    "userId": "usmee"
}

response = requests.post(url, json=data)



