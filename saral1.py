import json
f='{"name":"anzum","class":"computer","age":34}'
c=json.loads(f)
print(type(c))
print(c)