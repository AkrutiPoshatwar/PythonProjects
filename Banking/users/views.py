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
        user_dict[transfer.from_account_id] -= transfer.amount
        user_dict[transfer.to_account_id] += transfer.amount

    return JsonResponse(user_dict)


def user_balance(request,pk):

    user = User.objects.get(pk=pk)
    transactions_list = Transaction.objects.all()
    user_dict={}

    user_dict[user.account_id]= user.current_balance

    for transfer in transactions_list:
        if transfer.from_account_id in user_dict:
            user_dict[transfer.from_account_id] -= transfer.amount

        elif transfer.to_account_id in user_dict:
            user_dict[transfer.to_account_id] += transfer.amount

    return JsonResponse(user_dict)










