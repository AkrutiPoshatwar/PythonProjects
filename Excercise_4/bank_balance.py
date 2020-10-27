import json

with open('transaction_log.json', 'r') as f:
    data = json.load(f)
bank_balance = {}

balance = 0

for j in range(len(data['bank_transactions'])):

    for i in range(len(data['users'])):

        if data['users'][i]['acc_id'] == data['bank_transactions'][j]['acc_id']:
            balance = data['users'][i]['current_balance']

            if data['bank_transactions'][j]['type'] == 'credit':
                balance = balance + data['bank_transactions'][j]['amount']
                data['users'][i]['current_balance'] = balance
            else:
                balance = balance - data['bank_transactions'][j]['amount']
                data['users'][i]['current_balance'] = balance

            bank_balance.update({data['users'][i]['acc_id']: balance})

print(bank_balance)

