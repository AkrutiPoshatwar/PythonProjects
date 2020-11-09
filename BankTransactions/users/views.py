from django.shortcuts import render
from django.http import HttpResponse
from users.models import User,Transaction
from django.http import JsonResponse

def bank_balance(request):

    user_list = User.objects.all()
    transactions_list= Transaction.objects.all()

    user_dict={}
    for user in user_list:
        user_dict[user.account_id] = user.current_balance

    for transfer in transactions_list:
       if transfer.amount<= user_dict[transfer.from_account_id.account_id]:
            user_dict[transfer.from_account_id.account_id] -= transfer.amount
            user_dict[transfer.to_account_id.account_id] += transfer.amount

    return JsonResponse(user_dict)


def user_balance(request,pk):

    user = User.objects.get(pk=pk)
    transactions_list = Transaction.objects.all()
    user_dict={}

    user_dict[user.account_id]= user.current_balance

    for transfer in transactions_list:
        if transfer.amount <= user_dict[user.account_id]:
            if transfer.from_account_id.account_id in user_dict:
                user_dict[transfer.from_account_id.account_id] -= transfer.amount

            elif transfer.to_account_id.account_id in user_dict:
                user_dict[transfer.to_account_id.account_id] += transfer.amount

    return JsonResponse(user_dict)


def transaction_count(request):

    user_list = User.objects.all()
    transactions_list = Transaction.objects.all()
    ordered_transactions_list = transactions_list.order_by('date')

    user_dict={}
    for user in user_list:
        user_dict[user.account_id] = {'credit':0,
                                      'debit':0,
                                      'invalid_transfers':[],
                                      'current_balance': user.current_balance}
    for transfer in ordered_transactions_list:
        if transfer.amount <= user_dict[transfer.from_account_id.account_id]['current_balance']:
            user_dict[transfer.from_account_id.account_id]['current_balance'] -= transfer.amount
            user_dict[transfer.to_account_id.account_id]['current_balance'] += transfer.amount

            user_dict[transfer.from_account_id.account_id]['debit'] +=1
            user_dict[transfer.to_account_id.account_id]['credit'] += 1
        else:
            user_dict[transfer.from_account_id.account_id]['invalid_transfers'].append(transfer.date)

    return JsonResponse(user_dict)


