import json
a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
add=input("if you want to add something in shopping list=")
user=input("which item you want to buy")
user1=int(input("how much quantity you want"))
for key in a:
    for value in a[key]:
        if value==user:
            a[key][value]=int(a[key][value])-user1
    if "y"==add:
        a[key][user]=user1
x=json.dumps(a,indent=4)
print(x)
print(a)





    