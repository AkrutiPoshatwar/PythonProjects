import json

with open('users_transfers_data.json') as f:
    data= json.load(f)

sorted_bank_transfers = sorted(data['bank_transfers'],key=lambda x : x['date'], reverse=False)

users_dict = {}

for user in data['users']:
    users_dict[user['account_id']] = {
                                      'credit':0,
                                      'debit':0,
                                      'invalid_transfers':[],
                                      'current_balance':user['current_balance']}

for transfer in sorted_bank_transfers:

    if transfer['amount'] <= users_dict[transfer['from_account_id']]['current_balance'] :
        users_dict[transfer['from_account_id']]['current_balance'] -= transfer['amount']
        users_dict[transfer['to_account_id']]['current_balance'] += transfer['amount']

        users_dict[transfer['from_account_id']]['debit'] += 1
        users_dict[transfer['to_account_id']]['credit'] += 1

    else:
        users_dict[transfer['from_account_id']]['invalid_transfers'].append(transfer['date'])


print(json.dumps(users_dict, indent=4))
