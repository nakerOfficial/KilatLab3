from os import path
import requests
import json
from bt import BT


FILE_NAME = "pass.txt"
URL = "https://jsonplaceholder.typicode.com/todos/1"
LOGIN = 'iura94'

# is file exist:
isExist = path.exists(FILE_NAME)

# create or read file:
f = open(FILE_NAME, "w+") if not isExist else open(FILE_NAME, "r")
contents = f.read().splitlines()
f.close()

resultsBT = BT().Generate(contents)
resultsBT = list(set(resultsBT))
print('::', resultsBT)

def query(password):
    payload = {'login': LOGIN, 'pass': password}
    r = requests.get(URL)
    # r = requests.post(URL, data=json.dumps(payload))
    return r.text, r.status_code

for a in resultsBT:
    text, status = query(a)

    print('\n')
    print('Password: ', a)
    print('Status: ', status)
    print('Request:', text)
