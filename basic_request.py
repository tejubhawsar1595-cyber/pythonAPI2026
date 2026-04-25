from urllib import response

import requests


base_url = "https://simple-books-api.glitch.me"

response = requests.get(f"{base_url}/status")


# To Check status code
print("Status Code : ",response.status_code)

#Status of jason response
print(response.json())      #['status'] = ['OK']
