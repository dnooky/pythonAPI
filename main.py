import requests

print("Hello from Kostya!")

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)