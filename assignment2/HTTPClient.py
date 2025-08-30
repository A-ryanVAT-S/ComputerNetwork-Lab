import requests

##POST
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "userID": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}

try:
    response = requests.post(url, json=data)
    print("\nfor post")
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.json())
except requests.exceptions.RequestException as e:
    print("POST request failed:", e)

response = requests.post(url, json=data)
print(response.json())

##GET
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url)
    print("\nGET")
    print(response.json())
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Body:", response.json())
except requests.exceptions.RequestException as e:
    print("GET request failed:", e)
