import requests
import json
import datetime



now = datetime.datetime.now()



headers = {'Content-Type': 'application/json; chearset=utf-8'}
data = {'bed_id': 4 ,'time':str(now)}
res = requests.post('http://3.134.120.190:8000/api/facility/incident/',  data=json.dumps(data), headers=headers)
print(str(res.status_code) + " | " + res.text)
# print(now)