from django.shortcuts import render
from django.http import HttpResponseRedirect
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail


def subscribe(request):
    if request.method == 'POST':
        mail.send_mail('Confirmação de inscrição',
                       MESSAGE,
                       'contato@eventex.com.br',
                       ['contato@eventex.com.br', 'matheus@lopes.com'])
        return HttpResponseRedirect('/inscricao/')
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)


MESSAGE = """
Email teste de Matheus
12345678901
contato@eventex.com.br
11984028729
"""
