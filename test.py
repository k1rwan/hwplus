import requests
import json

host = input("host: ")
user = "NoUser"
headers = {"token":""}

while True:
    command = input(user + ">")
    commands = command.split(" ")
    
    if commands[0] == 'login':
        rsp = requests.post("http://" + host + "/login/", data={"username":commands[1],"password":commands[2]})
        try:
            user = rsp.json()['data']['username']
            headers['token'] = rsp.headers['token']
        except:
            print("No User")
        continue
    
    if commands[0] == 'get':
        rsp = requests.get("http://" + host + commands[1], headers=headers)
        try:
            print("JSONResponse: ")
            print(rsp.json())
        except:
            continue

    if commands[0] == 'post':
        rsp = requests.post("http://" + host + commands[1], data=eval(commands[2]),headers=headers)
        try:
            print("JSONResponse: ")
            print(rsp.json())
        except:
            continue

    if commands[0] == 'put':
        rsp = requests.put("http://" + host +commands[1], data=eval(commands[2]), headers=headers)
        try:
            print("JSONResponse: ")
            print(rsp.json())
        except:
            continue
