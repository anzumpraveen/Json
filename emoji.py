from pprint import pprint
import json
file= open("emoji.json")
data= json.load(file)

user=input("enter the title=")
for key in data:
    for value in key:
        if user==key[value]:
            print(key["symbol"])
            print(key["keywords"])