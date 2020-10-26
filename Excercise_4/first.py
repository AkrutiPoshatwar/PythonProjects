import json

with open('data_file.json','r') as f:
    data = json.load(f)

total = 0
for item in range(0, len(data)):
    total = total + data[item]

print('Total of the numbers is:',total)

with open('sum.json', 'w') as json_file:
  json.dump(total, json_file)