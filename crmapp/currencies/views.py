from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse

from .forms import CurrencyForm
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

from .models import Currency
from django.shortcuts import get_object_or_404

class CurrencyList(ListView):
    model = Currency
    paginator = Paginator(Currency, 12)
    template_name = 'currencies/currency_list.html'
    context_object_name = 'currencies'

    def get_queryset(self):
        try:
            a = self.request.GET.get('currency',)
        except KeyError:
            a = None
        if a:
            currency_list = Currency.objects.filter(
                currency_name__icontains=a,
                owner=self.request.user
            )
        else:
            currency_list = Currency.objects.filter(owner=self.request.user)
        return currency_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CurrencyList, self).dispatch(*args, **kwargs)

@login_required()
def currency_detail(request, uuid):

    currency = Currency.objects.get(uuid=uuid)
    if currency.owner != request.user:
            return HttpResponseForbidden()

    variables = {
        'currency': currency,
    }

    return render(request, 'currencies/currency_detail.html', variables)

@login_required()
def currency_cru(request, uuid=None):

    if uuid:
        currency = get_object_or_404(Currency, uuid=uuid)
        if currency.owner != request.user:
            return HttpResponseForbidden()
    else:
        currency = Currency(owner=request.user)

    if request.POST:
        form = CurrencyForm(request.POST, instance=currency)
        if form.is_valid():
            currency = form.save(commit=False)
            currency.owner = request.user
            currency.save()
            redirect_url = reverse(
                currency_detail,
                args=(currency.uuid,)
            )
            return HttpResponseRedirect(redirect_url)
    else:
        form = CurrencyForm(instance=currency)

    variables = {
        'form': form,
        'currency': currency
    }

    template = 'currencies/currency_cru.html'

    return render(request, template, variables)