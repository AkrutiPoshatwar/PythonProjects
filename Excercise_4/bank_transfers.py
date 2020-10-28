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
for user in data['users']:
    users_dict[user['account_id']] = user['current_balance']

try:
    if from_account in users_dict.keys() and to_account in users_dict.keys() and transfer_amount <= users_dict[from_account]:
        users_dict[from_account] -= int(transfer_amount)
        users_dict[to_account] += int(transfer_amount)
    else:
        raise IncorrectAccountId

except IncorrectAccountId as e:
    print(e)
    exit()
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

