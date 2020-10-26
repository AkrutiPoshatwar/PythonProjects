import json

with open('jsonfile.json','r') as f:
    data = json.load(f)

count = {}
for i in data:
    count[i] = count.get(i, 0) + 1
print(count)