import requests
import json
import time

# class API():
#     def __init__(self, usr, pwd, deploy):
#         self.usr = usr
#         self.pwd = pwd
#         self.deploy = deploy
#     def auth(usr, pwd):
#         auth = requests.post('https://f9p8bba1.ce.automationanywhere.digital/v1/authentication', data=json.dumps({'username:': usr, 'password': pwd}), proxies=proxies)
#         print(auth)

def control_room_auth(usr, pwd, proxies = {}):
    '''
    usr: username to control room
    pwd: password to control room
    proxies: 
    Function returns dictionary containing status code of the request and token if available.
    '''
    url = 'https://f9p8bba1.ce.automationanywhere.digital/v1/authentication'
    auth_data = {
        'username': usr,
        'password': pwd
    }
    authentication = requests.post(url, data=json.dumps(auth_data), proxies=proxies)
    return {'code': authentication.status_code, 'token': (json.loads((authentication.content).decode('utf-8')))['token']}

def activity_list(token, proxies = {}):
    headers = {'X-Authorization': token}
    filters = {
        "fields": [
            "string"
        ],
        "filter": {
            "operator": "NONE",
            "operands": [],
            "field": "string",
            "value": "string"
        },
        "sort": [
            {
            "field": "string",
            "direction": "asc"
            }
        ],
        "page": {
            "offset": 0,
            "length": 0
            }
        }
    url = 'https://f9p8bba1.ce.automationanywhere.digital/v2/activity/list'
    l = requests.post(url=url, data=json.dumps(filters), proxies=proxies, headers=headers)
    print(l.content)



if __name__ == "__main__":
    usr = 'piotr.grynczel@gds.ey.com'
    pwd = '2vgzvnri1'
    proxies = {
        'http': 'http://empweb1.ey.net:8080',
        'https': 'http://empweb1.ey.net:8080'
    }
    auth = control_room_auth(usr=usr, pwd=pwd, proxies=proxies)
    if auth['code'] == 200:
        print('OK!')
        # print(auth['token'])
        time.sleep(1)
        activity_list(auth['token'], proxies=proxies)
    else:
        print('----------------AUTH ERROR----------------')
        print(auth['code'])
        print('There was problem with authentication.')