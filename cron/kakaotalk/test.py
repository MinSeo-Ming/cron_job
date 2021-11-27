import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'd153e14bfad1b0d801b8533eb34bc37b'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'Cfcn8Nn6ZY6-DK2FhGSYnyP_YXLqIgrEZSo7HY9G32K7WsgxSyy6anNoY2sslwzPhV407QorDR4AAAF9YElWDQ'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

with open("../json/kakao_code.json","w") as fp:
    json.dump(tokens, fp)