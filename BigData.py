import requests
import json


headers = {'Content-Type': 'application/json; chearset=utf-8'}
# ['id', 'elder_id', 'time', 'lay', 'sit', 'empty', 'recent_status', 'today_status', 'max_status']
data = {'elder_id': 4 ,'time':"18:20",'lay':0,'sit':0,'empty':0,'recent_status':'lay','today_status':'sit','max_status':'sit'}
res = requests.post('http://3.134.120.190:8000/api/facility/occupancy/',  data=json.dumps(data), headers=headers)
print(str(res.status_code) + " | " + res.text)