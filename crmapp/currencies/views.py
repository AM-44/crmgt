from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

from .models import Currency

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