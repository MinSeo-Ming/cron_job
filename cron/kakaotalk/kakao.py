import requests
import json
import boto3
import datetime
from PIL import Image
import matplotlib.pyplot as plt

with open("../json/kakao_code.json", "r") as fp:
    tokens = json.load(fp)

# def get_graph(id):
#     s3 = boto3.resource('s3')
#     bucket = s3.Bucket('ssf-graph-team2')
#     now = (datetime.datetime.now()- datetime.timedelta(days=1)).strftime('%Y-%m-%d')
#     # print(now)
#     # 만약 실제로 돌릴거면 d -1일 해야함
#     object = bucket.Object(str(id)+'/'+now+'.png')
#     response = object.get()
#     file_stream = response['Body']
#     img = Image.open(file_stream)
#     # plt.show(img)
#     # img.show()
#     return img

def send_all_companion():
    pass

def send_talk(id):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    now = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    # img ="https://ssf-graph-team2.s3.us-east-2.amazonaws.com/"+str(id)+"/"+now+".png"
    img ="https://ssf-graph-team2.s3.us-east-2.amazonaws.com/"+str(1)+"/"+now+".png"

    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    data = {"template_object": json.dumps({"object_type": "feed",
                                           "content": {"title": 'test' , "description": "graph",
                                                       "image_url": img, "image_width": 700, "image_height": 289,
                                                       "link": {"web_url": url}}})}


    response = requests.post(url, headers=headers, data=data)
    response.status_code

# send_talk()