###########################################################
## The response is formatted as JSON
## How do we read individual fields from the JSON response?
## The "Type" function tells what data type it is

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://192.168.189.100:8080/platform/7/protocols/nfs/exports"
auth = HTTPBasicAuth('admin', 'abcd1234')
data = {
	'paths':[
		'/ifs/test2'
	]
}
        
response = requests.post(url=url, auth=auth, json=data, verify=False)

print response.content
