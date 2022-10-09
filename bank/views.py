from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Card, Transaction
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.decorators import login_required


@login_required
def account(request):
    usr = get_user(request)
    context = {
        'accs': Account.objects.filter(owner=usr)
    }
    return render(request, 'bank/u_account.html', context)


class AccountDetailView(DetailView):
    model = Account


@login_required
def card(request):
    usr = get_user(request)
    accs = list(Account.objects.filter(owner=usr).values())
    context = {
        'cards': Card.objects.filter(acc_c=accs)
    }
    return render(request, 'bank/u_cards.html', context)

@login_required
def transaction(request):
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'bank/u_transaction.html', context)


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>sjyfsuyf</h1>')
