from django.shortcuts import render
from django.http import HttpResponse
from bank.models import User
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
   
def create_card(request):
     if request.method =='POST':
        fname = request.POST.get('fname1')
        lname = request.POST.get('lname1')    
        pan_number = request.POST.get('pnumber1')
        if request.POST.get('pnumber'):#checking of pannumber from db
            return render(request, 'bank/create_account.html',{'error':True})
        else:
            Cnum = request.POST.get('Cnumber')
            Ctype = request.POST.get('Cards')    
            pin = request.POST.get('Cpin')
            limit = request.POST.get('Climits')    

def create_account(request):
     if request.method =='POST':
        fname = request.POST.get('fname1')
        lname = request.POST.get('lname1')    
        pan_number = request.POST.get('pnumber1')
        if request.POST.get('pnumber')!=:
            return render(request, 'bank/create_account.html',{'error':True})
        else:
            u_anumber = request.POST.get('Anumber')
            u_atype = request.POST.get('Atype')
            return render(request, 'bank/create_account.html')

def sign_up(request):
    if request.method =='POST':
        u_fname = request.POST.get('fname')
        u_lname = request.POST.get('lname')    
        u_email = request.POST.get('email')
        u_add1=request.POST.get('address1')
        u_add2=request.POST.get('address2')
        u_contact = request.POST.get('cnumber')
        u_pan_number = request.POST.get('pnumber')
        u_dob = request.POST.get('dob')
        u_gen=request.POST.get('gender')
        en=User(u_fname=u_fname,u_lname=u_lname,u_email=u_email,u_add1=u_add1,u_add2=u_add2,u_contact=u_contact,u_pan_number=u_pan_number,u_dob=u_dob,u_gender=u_gen)
        return render(request, 'bank/sign_up.html')


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>sjyfsuyf</h1>')
