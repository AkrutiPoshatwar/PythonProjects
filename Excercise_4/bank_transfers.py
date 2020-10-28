import json
import datetime

with open('bank_transfers_data.json') as f:
    data = json.load(f)

from_account = input('From account number:')
to_account = input('To account number:')
transfer_amount = int(input('Enter amount:'))

class IncorrectAccountId(Exception):
    def __init__(self, message = "Account Id does not exist"):
        self.message = message
    def __str__(self):
        return self.message

users_dict = {}

account_ids =[]
for user in data['users']:
    account_ids.append(user['account_id'])
    print(account_ids)

for user in data['users']:
    users_dict[user['account_id']] = user['current_balance']

    try:
        if user['account_id'] == str(from_account):
            users_dict[user['account_id']] -= int(transfer_amount)

        elif user['account_id'] == str(to_account):
            users_dict[user['account_id']] += int(transfer_amount)

        elif str(from_account) not in account_ids or str(to_account) not in account_ids :
            raise IncorrectAccountId()

    except IncorrectAccountId as e:
        print(e)
        exit()

print(users_dict)

transfer_info = {'from_account_id':from_account,
                 'to_account_id':to_account,
                 'amount':transfer_amount,
                 'date':str(datetime.datetime.utcnow())}

print(transfer_info)

data['bank_transfers'].append(transfer_info)

for user in data['users']:
    user['current_balance'] = users_dict[user['account_id']]

with open('bank_transfers_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)


