import json
f={"name":"anzum","class":"computer","age":34}
with open('anzum.json', 'w') as fp:
    json.dump(f, fp,indent=4)
