import json

with open('users_transfers_data.json') as f:
    data= json.load(f)

sorted_bank_transfers = sorted(data['bank_transfers'],key=lambda x : x['date'], reverse=True)

users_dict = {}
for user in data['users']:
    users_dict[user['account_id']] = user['current_balance']

invalid_transfers = {}
dates_list = []

for transfer in sorted_bank_transfers:
    if transfer['amount'] <= users_dict[transfer['from_account_id']]:
        users_dict[transfer['from_account_id']] -= transfer['amount']
        users_dict[transfer['to_account_id']] += transfer['amount']

    else:
        invalid_transfers.update({transfer['from_account_id']:transfer['date']})

print(dates_list)
print(invalid_transfers)


credited_to = {}
debited_to ={}

for key in users_dict:
    debit_count = 0
    credit_count = 0

    for transfer in sorted_bank_transfers:

        if key == transfer['from_account_id']:
            debit_count+=1
        elif key == transfer['to_account_id']:
            credit_count +=1

    credited_to[key] = credit_count
    debited_to[key] = debit_count

transfer_info={}

for key in users_dict:
    transfer_info['credits'] = credited_to[key]
    transfer_info['debits'] = debited_to[key]
    transfer_info['Invalid_transfer'] = invalid_transfers[key]
    transfer_info['current_balance'] = users_dict[key]

    print(key,":",json.dumps(transfer_info, indent=4))



