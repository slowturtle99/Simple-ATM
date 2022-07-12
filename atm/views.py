from django.shortcuts import HttpResponse, render, get_object_or_404, redirect

from .models import Card, Account
from .forms import DepositForm, WithdrawForm
from django.utils import timezone
# Create your views here.

def card(request):
    context = None
    return render(request, 'atm/card.html', context)

def card_find(request):
    card_number = request.GET['card_number']
    pin_number = request.GET['pin_number']
    if pin_check(card_number, pin_number):
        return redirect('atm:account_list', card_number)
    return redirect('atm:card')

def pin_check(card_number, pin_number):
    if pin_number == card_number[-4:]:
        return True
    return False

def list_accounts(request, card_number):
    card = get_object_or_404(Card, card_number=card_number)
    card_account_pair_list = card.cardaccountpair_set.all()
    context = {'card_account_pair_list': card_account_pair_list}
    return render(request, 'atm/account_list.html', context)

def actions(request, account_number):
    account = get_object_or_404(Account, account_number=account_number)
    context = {'account': account}
    return render(request, 'atm/actions.html', context)

def balance(request, account_number):
    account = get_object_or_404(Account, account_number=account_number)
    context = {'account': account}
    return render(request, 'atm/balance.html', context)

def deposit(request, account_number):
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

def withdraw(request, account_number):
    account = get_object_or_404(Account, account_number=account_number)
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.account = account
            deposit.timestamp = timezone.now()
            account.balance -= deposit.amount
            deposit.balance = account.balance
            deposit.save()
            account.save() 
            return redirect('atm:actions', account_number)
    else:
        form = WithdrawForm()

    context = {"form": form, 'account': account}
    return render(request, 'atm/withdraw.html', context)


def report(request, account_number):
    account = get_object_or_404(Account, account_number=account_number)
    deposit_list = account.deposit_set.order_by('timestamp')
    withdraw_list = account.withdraw_set.order_by('timestamp')
    context = {
        'account': account,
        'deposit_list': deposit_list,
        'withdraw_list': withdraw_list
        }
    return render(request, 'atm/report.html', context)