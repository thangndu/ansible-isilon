###########################################################
## The response is formatted as JSON
## How do we read individual fields from the JSON response?
## The "Type" function tells what data type it is

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://192.168.189.100:8080/namespace/ifs"
auth = HTTPBasicAuth('admin', 'abcd1234')

response = requests.get(url=url, auth=auth, verify=False)

obj = json.loads(response.content)

for c in obj['children']:
    print c['name']