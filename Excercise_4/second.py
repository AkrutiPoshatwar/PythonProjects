import json

with open('data_file.json') as f:
    data = json.load(f)

count = {}
for i in data:
    count[i] = count.get(i, 0) + 1
print(count)


with open('frequency.json', 'w') as json_file:
  json.dump(count, json_file)