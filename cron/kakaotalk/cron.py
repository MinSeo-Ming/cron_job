import requests
import json
import boto3
import datetime
from PIL import Image
import matplotlib.pyplot as plt

with open("../json/kakao_code.json", "r") as fp:
    tokens = json.load(fp)

def get_graph(id):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('ssf-graph-team2')
    now = (datetime.datetime.now()- datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    # print(now)
    # 만약 실제로 돌릴거면 d -1일 해야함
    object = bucket.Object(str(id)+'/'+now+'.png')
    response = object.get()
    file_stream = response['Body']
    img = Image.open(file_stream)
    # plt.show(img)
    # img.show()
    return img


def send_talk():
    # graph = get_graph(1)
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    now = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    img ="https://ssf-graph-team2.s3.us-east-2.amazonaws.com/"+str(1)+now+".png"

    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    data = {
        "template_object": {
            "object_type": "feed",
            "content":{
                "title":"그래프",
                "description":"흐어어ㅓ",
                "image_url": img,
                "image_width":640,
                "image_height":640,
            },
            "social": {
                "like_count": 100,
                "comment_count": 200,
                "shared_count": 300,
                "view_count": 400,
                "subscriber_count": 500
            },
            "buttons": [
                {
                    "title": "웹으로 이동",
                    "link": {
                        "web_url": "http://www.daum.net",
                        "mobile_web_url": "http://m.daum.net"
                    }
                },
                {
                    "title": "앱으로 이동",
                    "link": {
                        "android_execution_params": "contentId=100",
                        "ios_execution_params": "contentId=100"
                    }
                }
            ]

        }
    }
    response = requests.post(url, headers=headers, data=data)
    response.status_code

send_talk()
# get_graph(1)