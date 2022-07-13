from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from .models import Card, Account
from .forms import DepositForm, WithdrawForm


def card_main(request):
    """
    Renders the main page of the atm.

    """
    context = None
    return render(request, 'atm/card.html', context)


def card_check(request):
    """
    Get the card informations and check pin numbers.
    Redirect to account list.

    Todo:
        To implement real atm system card informations should be obtained 
        from the card reader device of ATM.

    """
    card_number = request.GET['card_number']
    pin_number = request.GET['pin_number']
    if pin_check(card_number, pin_number):
        return redirect('atm:account_list', card_number)
    return redirect('atm:card')


def pin_check(card_number, pin_number):
    """
    Check PIN number is correct or not.
    This is temporal implementaion.
    PIN number is correct if it is same as last four number of the card number. 

    Args:
        card_number (str): Card number.
        pin_number (str): PIN number.

    Todo:
        Implement authentication using bank API.


    """
    if pin_number == card_number[-4:]:
        return True
    return False


def list_accounts(request, card_number):
    """
    Shows the list of accounts linked to the card.

    Args:
        card_number (str): Card number.

    """
    card = get_object_or_404(Card, card_number=card_number)
    card_account_pair_list = card.cardaccountpair_set.all()
    context = {'card_account_pair_list': card_account_pair_list}
    return render(request, 'atm/account_list.html', context)


def select_action(request, account_number):
    """
    Shows the possible actions for the account.

    Args:
        account_number (str): Account number.

    """
    account = get_object_or_404(Account, account_number=account_number)
    context = {'account': account}
    return render(request, 'atm/actions.html', context)


def balance(request, account_number):
    """
    Shows the balance of the account.

    Args:
        account_number (str): Account number.

    """
    account = get_object_or_404(Account, account_number=account_number)
    context = {'account': account}
    return render(request, 'atm/balance.html', context)


def deposit_money(request, account_number):
    """
    Deposit money into account.

    Args:
        account_number (str): Account number.

    """
    account = get_object_or_404(Account, account_number=account_number)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.account = account
            deposit.timestamp = timezone.now()
            account.balance += deposit.amount
            deposit.balance = account.balance
            deposit.save()
            account.save()
            return redirect('atm:actions', account_number)
    else:
        form = DepositForm()

    context = {"form": form, 'account': account}
    return render(request, 'atm/deposit.html', context)


def withdraw_money(request, account_number):
    """
    Withdraw money from account.

    Args:
        account_number (str): Account number.

    """
    account = get_object_or_404(Account, account_number=account_number)
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            withdraw = form.save(commit=False)
            withdraw.account = account
            withdraw.timestamp = timezone.now()
            account.balance -= withdraw.amount
            withdraw.balance = account.balance
            withdraw.save()
            account.save()
            return redirect('atm:actions', account_number)
    else:
        form = WithdrawForm()

    context = {"form": form, 'account': account}
    return render(request, 'atm/withdraw.html', context)


def transaction_history(request, account_number):
    """
    Shows the transaction history of the account.

    Args:
        account_number (str): Account number.

    """
    account = get_object_or_404(Account, account_number=account_number)
    deposit_list = account.deposit_set.order_by('timestamp')
    withdraw_list = account.withdraw_set.order_by('timestamp')
    context = {
        'account': account,
        'deposit_list': deposit_list,
        'withdraw_list': withdraw_list
        }
    return render(request, 'atm/report.html', context)
