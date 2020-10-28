import json
import datetime

with open('bank_transfers_data.json') as f:
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


transfer_info = {'from_account_id':from_account,
                 'to_account_id':to_account,
                 'amount':transfer_amount,
                 'date':str(datetime.datetime.now())}

data['bank_transfers'].append(transfer_info)
for user in data['users']:
    user['current_balance'] = users_dict[user['account_id']]

with open('bank_transfers_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(data['bank_transfers'])



