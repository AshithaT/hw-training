import requests

# s = requests.Session()

# s.get('https://httpbin.org/cookies/set/sessioncookie/user1234')
# r = s.get('https://httpbin.org/cookies')

# print(r.text)

# #s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})

# # both 'x-test' and 'x-test2' are sent
# s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})

# s = requests.Session()

# r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print(r.text)
# # '{"cookies": {"from-my": "browser"}}'

# r = s.get('https://httpbin.org/cookies')
# print(r.text)
# # '{"cookies": {}}'

with requests.Session() as s:
    s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')