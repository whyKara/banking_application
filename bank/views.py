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


class NewTransactionView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['t_facc', 't_tacc', 't_ammount', 't_revert_req', 't_status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        # amount=form.instance('t_amount')
        facc = Account.objects.get(acc_no=form.instance.t_facc)
        facc.acc_balance -= int(form.instance.t_ammount)
        facc.save()
        tacc = Account.objects.get(acc_no=form.instance.t_tacc)
        tacc.acc_balance += int(form.instance.t_ammount)
        tacc.save()
        def get_success_url(self):
            return reverse('Transaction-Details')
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
