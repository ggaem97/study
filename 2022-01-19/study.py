# import json
# import sys
# user = {
#     "id" : "dkwlwjdals",
#     "password" : "123456",
#     "hobby" : ["dance", "talk"]
# }
#
#
# data = json.dumps(user, indent=4)
# print(data)
# f = open('data.json', 'w')
# f.write(data)
#
#
# d = json.loads(data)
# print(d)
# f.close()


import requests
import json
response = requests.get(url="https://jsonplaceholder.typicode.com/users")
print(response)

data = response.json()
# print(data)

namelst = []
emailLst = []
for user in data:
    namelst.append(user['name'])
    emailLst.append(user['email'])
# print(namelst)
print(emailLst)