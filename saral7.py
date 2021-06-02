import json
filename = 'data.txt'
dict1 = {}
with open(filename) as f:
    for line in f:
        c,des = line.strip().split(None,1)
        dict1[c] = des.strip()      
out_file=open("saral7.json", "w")
json.dump(dict1, out_file,indent = 4)
out_file.close()   

  
  
