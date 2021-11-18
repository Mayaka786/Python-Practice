import requests
response=requests.get("https://www.bit.ly/vl-udemy")
print(response.status_code)
