from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


accs = [
    {
        'account_name': 'Account1',
        'account_no': 'XXXXXXXXXXXXX1278',
    },
    {
        'account_name': 'Account 2',
        'account_no': 'XXXXXXXXXXXXX1289',
    },
    {
        'account_name': 'Account 1',
        'account_no': 'XXXXXXXXXXXXX1278',
    },
    {
        'account_name': 'Account 2',
        'account_no': 'XXXXXXXXXXXXX1289',
    },
    {
        'account_name': 'Account 1',
        'account_no': 'XXXXXXXXXXXXX1278',
    },
    {
        'account_name': 'Account 2',
        'account_no': 'XXXXXXXXXXXXX1289',
    },

]


cards = [
    {
        'card_type': 'Debit Card',
        'card_no': '218361983382173712',
    },
    {
        'card_type': 'Credit Card',
        'card_no': '218361983382173712',
    },
]

transactions = [
    {
        'from_acc': 'XXXXXXXXXXXXX1278',
        'to_acc': 'XXXXXXXXXXXXX1289',
        'amount': '50000',
        't_status': True
    },
    {
        'from_acc': 'XXXXXXXXXXXXX1278',
        'to_acc': 'XXXXXXXXXXXXX1289',
        'amount': '30000',
        't_status': False
    },
    {
        'from_acc': 'XXXXXXXXXXXXX1278',
        'to_acc': 'XXXXXXXXXXXXX1289',
        'amount': '57000',
        't_status': True
    },
    {
        'from_acc': 'XXXXXXXXXXXXX1278',
        'to_acc': 'XXXXXXXXXXXXX1289',
        'amount': '8900',
        't_status': True
    },

]


def account(request):
    context = {
        'accs': accs
    }
    return render(request, 'bank/u_account.html', context)


def card(request):
    context = {
        'cards': cards
    }
    return render(request, 'bank/u_cards.html', context)


def transaction(request):
    context = {
        'transactions': transactions
    }
    return render(request, 'bank/u_transaction.html', context)


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>sjyfsuyf</h1>')
