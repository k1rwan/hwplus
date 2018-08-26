urlprefix = "http://localhost:8000"

gql_url = urlprefix + '/graphql/'

gql = """query {
        allCourses {
            courseAssignments {
                id
            }
        }
}"""

import requests

headers = {
    "token": "ImxpYWRyaW56Ig.DmGnrA.SOFm9tdX4CHunl27FfXbLp_q5UA"
}

data = {
    "query": gql
}

rsp = requests.post(gql_url, data=data, headers=headers)

print(rsp.json())
