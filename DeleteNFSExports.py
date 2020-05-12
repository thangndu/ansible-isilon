###########################################################
## The response is formatted as JSON
## How do we read individual fields from the JSON response?
## The "Type" function tells what data type it is

import requests
from requests.auth import HTTPBasicAuth
import json
import sys

nfs_export_id = sys.argv[1]
print nfs_export_id

url = "https://192.168.189.100:8080/platform/7/protocols/nfs/exports/" + nfs_export_id

auth = HTTPBasicAuth('admin', 'abcd1234')
        
response = requests.delete(url=url, auth=auth, verify=False)

print response.content
