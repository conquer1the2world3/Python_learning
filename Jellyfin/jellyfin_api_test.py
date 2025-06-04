import requests

url = "http://127.0.0.1:8096/Auth/Keys"
headers = {"Authorization": "MediaBrowser Token=8ea4dba65e6446bc81104e5001d6714c"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response. content.decode())
else:
    print("Error:", response.status_code)