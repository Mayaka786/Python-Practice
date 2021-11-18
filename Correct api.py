import requests
response=requests.get("https://www.bit.ly/vl-udemy")
fox= response.json{}
print(fox['image'])
