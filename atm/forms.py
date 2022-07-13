from django import forms
from .models import Deposit, Withdraw


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount']
        labels = {
            'amount': '금액',
        }

class  WithdrawForm(forms.ModelForm):
    class Meta:
        model =  Withdraw
        fields = ['amount']
        labels = {
            'amount': '금액',
        }
