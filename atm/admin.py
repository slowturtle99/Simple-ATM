from django.contrib import admin

# Register your models here.

from .models import Card, Account, CardAccountPair, Deposit, Withdraw

admin.site.register(Card)
admin.site.register(Account)
admin.site.register(CardAccountPair)
admin.site.register(Deposit)
admin.site.register(Withdraw)
