from django.db import models

class Card(models.Model):
    card_number = models.CharField(max_length=20, unique=True)

class Account(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField(default=0)

class CardAccountPair(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

class Deposit(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    balance = models.IntegerField()
    timestamp = models.DateTimeField()

class Withdraw(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    balance = models.IntegerField()
    timestamp = models.DateTimeField()
