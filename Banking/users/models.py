from django.db import models

class User(models.Model):
    account_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    current_balance = models.IntegerField(default=0)


class Transaction(models.Model):
    from_account_id = models.CharField(max_length=100)
    to_account_id = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField('User', related_name='transactions')


