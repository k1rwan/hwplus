import requests

url = 'http://localhost:8000/graphql/'

headers = {
    'token': 'ImxpYWRyaW56Ig.Dp2-Kw.fgMMPjeoajusU7mqBv4d-9B-_38'
}

gql = """
mutation {
    createSubmission (
        submissionData: {
            image: 1,
            assignment: 6,
            description: "卢姥爷，这是我的作业"
        }
    ) {
        ok
    }
}
"""

data = {
    'query': gql
}

resp = requests.post(url, data=data, headers=headers)

print(resp.text)