from django.shortcuts import render
from django.http import HttpResponse
from .models import create_account
from django.db import connections
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
   
def create_account(request):
    if request.method =='POST':

    return render(request, 'bank/create_account.html',{})

def sign_up(request):
    if request.method =='POST':
        u_fname = request.POST.get['fname']
        u_lname = request.POST.get['lname']    
        u_email = request.POST.get['email']
        u_add1=request.POST.get['address1']
        u_add2=request.POST.get['address2']
        u_contact = request.POST.get['cnumber']
        u_pan_number = request.POST.get['pnumber']
        u_dob = request.POST.get['dob']
        u_gender=request.POST.get['gender']
        return render(request, 'bank/sign_up.html',{})


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>sjyfsuyf</h1>')
