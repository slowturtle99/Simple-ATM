from django import forms
from .models import Deposit, Withdraw


class DepositForm(forms.ModelForm):
    """
    Form for Deposit model.

    Fields:
        amount (int): Amount of money to deposit.

    """
    class Meta:
        model = Deposit
        fields = ['amount']
        labels = {
            'amount': '금액',
        }

class  WithdrawForm(forms.ModelForm):
    """
    Form for Deposit model.

    Fields:
        amount (int): Amount of money to deposit.

    """
    class Meta:
        model =  Withdraw
        fields = ['amount']
        labels = {
            'amount': '금액',
        }
