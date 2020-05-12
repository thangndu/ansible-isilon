###########################################################
## The response is formatted as JSON
## How do we read individual fields from the JSON response?
## The "Type" function tells what data type it is

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://192.168.189.100:8080/platform/7/cluster/config"
auth = HTTPBasicAuth('admin', 'abcd1234')

response = requests.get(url=url, auth=auth, verify=False)

obj = json.loads(response.content)

cluster_name = obj['name']
number_of_node = len(obj['devices'])
onefs_version = obj['onefs_version']['release']

print "Cluster name: " + cluster_name
print "Number of node: " + str(number_of_node)
print "OneFS version: " + onefs_version
