import json
l1=["neelam","programer","24","2400"]
l2=["komal","trainer","24","20000"]
l3=["anuradha","HR","25","40000"]
l4=["Abhishek","manager","29","63000"]
l5=["name","discreaption","age","salary"]
dict1 = {} 
dict2 = {}
dict3 = {}
dict4 = {}
dict5 = {}
i=0
while i<len(l1):
    j=0    
    while j<len(l5):
        dict1[l5[j]]=l1[j]
        dict2[l5[j]]=l2[j]
        dict3[l5[j]]=l3[j]
        dict4[l5[j]]=l4[j]
        j+=1
    dict5["emp1"]=dict1
    dict5["emp2"]=dict2
    dict5["emp3"]=dict3
    dict5["emp4"]=dict4
    i+=1
data=json.dumps(dict5,indent=4)
print(data)
print(type(data))
