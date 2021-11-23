import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/kakaotalk')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'd153e14bfad1b0d801b8533eb34bc37b'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'rhwJkNfOWV6OJLU2oLRysstvui4_zgRMvL6rQY2lhlzbham2UIZDeYatrQuqNlL3CDlLuAorDNMAAAF9PEmZtA'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("../json/kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

