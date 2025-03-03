import requests

url = "http://127.0.0.1:8080/employees/3"
data = {
    "name": "Tri Le Duc",
    "department": "NeurondAI"
}
# response = requests.post(url, json=data)
# response = requests.put(url, json=data)
response = requests.delete(url)

print(response.json())  # Prints the response
