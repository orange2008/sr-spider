import json
import os
import requests
import libreq
usr = input("Username: ")
print("Requesting...")
query = "https://api.github.com/users/" + usr
raw_data = requests.get(query)
print("Status Code: " + str(raw_data.status_code))
if raw_data.status_code != 200:
    print("Request failed, please check your username and your Internet Connection.")
else:
    libreq.get(raw_data.json())
