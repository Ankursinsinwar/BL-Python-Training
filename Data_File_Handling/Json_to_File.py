import json

dist = {"name":"Ankur",
        "age":22,
        "city":"Mathura",
        "education":{
            "degree": "B.Tech",
            "major": "Computer Science",
            "university": "GLA University"
        }}

try:
    data = json.load(open("Assets\\data.json",'r'))
except:
    data = []

data.append(dist)
json.dump(data, open("Assets\\data.json",'w'))

print(data)