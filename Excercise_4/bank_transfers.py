import json

with open('bank_transfers.json') as f:
    data = json.load(f)

from_account = input('From account number:')
to_account = input('To account number:')
transfer_amount = int(input('Enter amount:'))

users_dict = {}

for user in data['users']:
    users_dict[user['account_id']] = user['current_balance']

    if user['account_id'] == str(from_account):
        users_dict[user['account_id']] -= int(transfer_amount)

    elif user['account_id'] == str(to_account):
        users_dict[user['account_id']] += int(transfer_amount)

print(users_dict)


