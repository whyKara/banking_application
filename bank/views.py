from django.shortcuts import render
from django.http import HttpResponse
from bank.models import User
from bank.models import Accounts
from bank.models import Cards
from django.db import connections
from .forms import UserForm
from .forms import AccountsForm
from .forms import CardsForm
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
   
def create_card(request):
     form=CardsForm()
     context={'Cform':form}
     if request.method =='POST':
        form=UserForm(request.post)
        if form.is_valid():
            form.save()
        context={'Cform':form}   
        return render(request, 'bank/create_card.html',context)
    

def create_account(request):
     form=AccountsForm()
     context={'Aform':form}
     if request.method =='POST':
        form=UserForm(request.post)
        if form.is_valid():
            form.save()
        context={'Aform':form}    
        return render(request, 'bank/create_account.html',context)

def sign_up(request):
    form=UserForm()
    context={'form':form}
    if request.method =='POST':
        form=UserForm(request.post)
        if form.is_valid():
            form.save()
        context={'form':form}    
        return render(request, 'bank/sign_up.html',context)


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>sjyfsuyf</h1>')
