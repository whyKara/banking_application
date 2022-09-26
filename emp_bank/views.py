from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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


def dashboard(request):
    context = {
        'transactions': transactions
    }
    return render(request, 'emp_bank/e_dashboard.html', context)


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>addwfawf</h1>')


def revert_notofi(request):
    context = {
        'transactions': transactions
    }
    return render(request, 'emp_bank/e_revert_notifi.html', context)
