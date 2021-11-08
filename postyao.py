import requests
import json
import random

with open('E:/前端基础/HTML/案例/HTML/yao.json','r',encoding='utf8')as fp:
    json_data = json.loads(fp.read())
    headers = {'Content-Type': 'application/json'}
    for i in json_data:
        list = []
        list.append(i)
        res = requests.post(url="http://47.111.186.107:9000/ruangong/pharmacy",headers = headers,data = json.dumps(list))
        print(res.json())
