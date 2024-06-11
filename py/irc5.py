import requests
# Define the URL

scheme = 'http://'
host = '127.0.0.1'
path = '/rw/rapid/execution'
auth_user = 'Default User'
auth_pw = 'robotics'

dictParams = {'json': '1'}
# dictParams = {}

# Send the GET request
url = scheme + host + path
response = requests.get(url, params=dictParams, auth=requests.auth.HTTPDigestAuth(auth_user, auth_pw))

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful!")
    # Print the response content
    print("Response Content:", response.text)
else:
    print("Failed to retrieve data")
    print("Status Code:", response.status_code)
    print("Response Content:", response.text)
