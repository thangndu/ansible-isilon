###########################################################
## The response is formatted as JSON
## How do we read individual fields from the JSON response?
## The "Type" function tells what data type it is

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://192.168.189.100:8080/namespace/ifs/test2"
auth = HTTPBasicAuth('admin', 'abcd1234')
headers = {
    'x-isi-ifs-target-type': 'container',
    'x-isi-ifs-access-control': 'public'
}
        
response = requests.put(url=url, auth=auth, headers=headers, verify=False)

print response.content
