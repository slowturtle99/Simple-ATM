from django.db import models

class Card(models.Model):
    """
    Model for card.

    Args:
        card_number (str): Card number. The typical length is 14~16.

    Todo:
        * Add arguments such as cvc_number, expiration date, etc. 

    """
    card_number = models.CharField(max_length=20, unique=True)

class Account(models.Model):
    """
    Model for account.

    Args:
        account_number (str): Account number. The typical length is 12~14.
        balance (int): The balance in account.

    """
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField(default=0)

class CardAccountPair(models.Model):
    """
    Model for linking accounts to a card.

    Args:
        account (Account): Account for linking.
        card (Card): Card to be linked.

    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

class Deposit(models.Model):
    """
    Model for logging deposit history.

    Args:
        account (Account): Account.
        amount (positive int): The amount of deposited money.
        balance (int): The balance of the account after deposit.
        timestamp (DateTime): Time stamp.

    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    balance = models.IntegerField()
    timestamp = models.DateTimeField()

class Withdraw(models.Model):
    """
    Model for logging withdraw history.

    Args:
        account (Account): Account.
        amount (positive int): The amount of withdrawed money.
        balance (int): The balance of the account after withdraw.
        timestamp (DateTime): Time stamp.

    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    balance = models.IntegerField()
    timestamp = models.DateTimeField()
