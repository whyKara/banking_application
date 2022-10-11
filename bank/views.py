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


class NewTransactionView(LoginRequiredMixin,CreateView):
    model = Transaction
    fields = ['t_facc', 't_tacc','t_ammount']

    def form_valid(self, form):
        form.instance.author = self.request.user
        facc=Transaction.objects.get(t_facc=)
        facc.amount-=int(amount)
        facc.save()
        tacc=Transaction.objects.get(t_tacc=)
        tacc.amount+=int(amount)
        tacc.save()
        return super().form_valid(form)

@login_required
def card(request):
    usr = get_user(request)
    context = {
        'cards': Card.objects.filter(acc_c=usr)
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
