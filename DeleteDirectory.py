###########################################################
## The response is formatted as JSON
## How do we read individual fields from the JSON response?
## The "Type" function tells what data type it is

import requests
from requests.auth import HTTPBasicAuth
import json


url = "https://192.168.189.100:8080/namespace/ifs/test2"
auth = HTTPBasicAuth('admin', 'abcd1234')
params = {
    'recursive': 'true'
}

response = requests.delete(url=url, auth=auth, params=params, verify=False)

print response.content
