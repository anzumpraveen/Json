import json
f = open('as.json')
data = json.load(f)
for i in data['detail']:
    print(i)
f.close()