import requests
import json


with open("../json/kakao_code.json","r") as fp:
    tokens =json.load(fp)


friend_url = "https://kapi.kakao.com/v1/api/talk/friends"
headers={"Authorization" : "Bearer " + tokens["access_token"]}
result = json.loads(requests.get(friend_url, headers=headers).text)

print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
print(friends_list)
# print(type(friends_list))
print("=============================================")
for i in friends_list:
    print(i.get("uuid"))
    friend_id = i.get("uuid")
    print(friend_id)

