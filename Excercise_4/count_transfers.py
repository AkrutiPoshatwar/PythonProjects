import json

with open('users_transfers_data.json') as f:
    data= json.load(f)

sorted_bank_transfers = sorted(data['bank_transfers'],key=lambda x : x['date'], reverse=False)

users_dict = {}
for user in data['users']:
    users_dict[user['account_id']] = user['current_balance']

invalid_transfers ={}
credited_to = {}
debited_to ={}


for transfer in sorted_bank_transfers:

    if transfer['amount'] <= users_dict[transfer['from_account_id']]:
        users_dict[transfer['from_account_id']] -= transfer['amount']
        users_dict[transfer['to_account_id']] += transfer['amount']


        if transfer['from_account_id'] in debited_to:
            debited_to[transfer['from_account_id']]+= 1

            print('hiii',debited_to[transfer['from_account_id']])
        else:
            debited_to.update({transfer['from_account_id']:1})

        if transfer['to_account_id'] in credited_to:
            credited_to[transfer['to_account_id']] += 1
        else:
            credited_to.update({transfer['to_account_id']: 1})


    else:
        if transfer['from_account_id'] in invalid_transfers:
            invalid_transfers[transfer['from_account_id']].append(transfer['date'])
        else:
            invalid_transfers[transfer['from_account_id']] = [transfer['date']]

print(invalid_transfers)


transfer_info={}
user_transfer_info ={}
for key in users_dict:
    transfer_info['credits'] = credited_to[key]
    transfer_info['debits'] = debited_to[key]
    transfer_info['Invalid_transfers'] = invalid_transfers[key]
    transfer_info['current_balance'] = users_dict[key]

    print(transfer_info['debits'])

    user_transfer_info[key] = transfer_info

print(json.dumps(user_transfer_info, indent=4))




