import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    print("Data fetched successfully.")
    data = response.json()
    # Display the first 5 post
    for post in data[:5]:
        print(f"Title: {post['title']}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    