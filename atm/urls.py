from django.urls import path

from . import views

app_name = 'atm'

urlpatterns = [
    path("", views.card_main, name="card_main"),
    path("card_check/", views.card_check, name="card_check"),
    path("account/<str:card_number>/", views.list_accounts, name="account_list"),
    path("actions/<str:account_number>/", views.select_action, name="actions"),
    path("deposit/<str:account_number>/", views.deposit_money, name="deposit_money"),
    path("withdraw/<str:account_number>/", views.withdraw_money, name="withdraw_money"),
    path("balence/<str:account_number>/", views.balance, name="show_balance"),
    path("transaction_history/<str:account_number>/", views.transaction_history, name="transaction_history"),
]
