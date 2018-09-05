urlprefix = "http://localhost:8000"

gql_url = urlprefix + '/graphql/'

gql = """query {
        getUsersByUsernames(usernames:["liadrinz","dimpurr"]) {
            buptId
        }
}"""

import requests

headers = {
    "token": "ImxpYWRyaW56Ig.DmaOkw.7jPjxAriGiTdlyU979eh_x3B0t8"
}

data = {
    "query": gql
}

rsp = requests.post(gql_url, data=data, headers=headers)

print(rsp.json())
