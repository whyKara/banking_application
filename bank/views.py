from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Card, Transaction


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
        'accs': Account.objects.all()
    }
    return render(request, 'bank/u_account.html', context)


def card(request):
    context = {
        'cards': Card.objects.all()
    }
    return render(request, 'bank/u_cards.html', context)


def transaction(request):
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'bank/u_transaction.html', context)


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>sjyfsuyf</h1>')
