import json
dict1 = {}
with open ("doc.txt") as fh:
    for line in fh:
        command,description = line.strip().split()
        dict1[command] = description.strip()
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()