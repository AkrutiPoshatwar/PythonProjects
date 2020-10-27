import json

with open('transaction_log.json', 'r') as f:
    data = json.load(f)

users_dict = {}
for user in data['users']:
    users_dict[user['account_id']] = user['current_balance']

for transaction in data['bank_transactions']:
    if transaction['account_id'] in users_dict:

        if transaction['type'] == 'credit':
            users_dict[transaction['account_id']] += transaction['amount']
        else:
            users_dict[transaction['account_id']] -= transaction['amount']

print(users_dict)