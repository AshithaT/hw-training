# Handling Response for HTTP Requests

# JSON Response

# import requests
# getdata = requests.get('https://jsonplaceholder.typicode.com/users')
# print(getdata.json())

# RAW response

# import requests
# getdata = requests.get('https://jsonplaceholder.typicode.com/users', stream=True)
# print(getdata.raw.read(50))

# BINARY response

# import requests
# getdata = requests.get('https://jsonplaceholder.typicode.com/users')
# print(getdata.content)

# GETTING response

# import requests
# getdata = requests.get('https://jsonplaceholder.typicode.com/users');    
# print(getdata.content)