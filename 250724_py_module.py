

# from my_math import ceil, floor

import requests    

url = "https://date.nager.at/api/v3/publicholidays/2025/KR"

response = requests.get(url).json() # .json ---> 딕셔너리

#response = requests.ger(url).json() # .text ---> json


print(response)