import json
f={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}

x=json.dumps(f,indent=4,sort_keys=True)
print(x)