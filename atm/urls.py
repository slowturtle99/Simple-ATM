from django.urls import path

from . import views

app_name = 'atm'

urlpatterns = [
    path("", views.card, name="card"),
    path("card_find/", views.card_find, name="card_find"),
    path("account/<str:card_number>/", views.list_accounts, name="account_list"),
    path("actions/<str:account_number>/", views.actions, name="actions"),
    path("deposit/<str:account_number>/", views.deposit, name="deposit_money"),
    path("withdraw/<str:account_number>/", views.withdraw, name="withdraw_money"),
    path("balence/<str:account_number>/", views.balance, name="show_balance"),
    path("report/<str:account_number>/", views.report, name="report_transactions"),
]