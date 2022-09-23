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


def home(request):
    context = {
        'accs': accs
    }
    return render(request, 'bank/u_account.html', context)


def account(request):
    return HttpResponse('<h1>account</h1>')
