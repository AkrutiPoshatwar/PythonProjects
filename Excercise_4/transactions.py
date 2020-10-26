import json

with open('transaction_log.json','r') as f:
    data = json.load(f)

enter_acc_number = input('enter acc number: ')

count = 0
for i in range(len(data['bank_transactions'])):
    if data['bank_transactions'][i]['acc_id']== enter_acc_number:
        count+=1
print(count)