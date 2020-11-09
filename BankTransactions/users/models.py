from django.db import models

class User(models.Model):

    account_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    current_balance = models.IntegerField(default=0)

class Transaction(models.Model):

    from_account_id= models.ForeignKey(to=User, null=True, related_name='from_account_id', on_delete=models.CASCADE)
    to_account_id = models.ForeignKey(to=User, null=True, related_name='to_account_id', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)