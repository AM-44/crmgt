from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Currency

class CurrencyList(ListView):
    model = Currency
    template_name = 'currencies/currency_list.html'
    context_object_name = 'currencies'

    def get_queryset(self):
        currency_list = Currency.objects.filter(owner=self.request.user)
        return currency_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CurrencyList, self).dispatch(*args, **kwargs)