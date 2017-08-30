from django.conf.urls import url
from views import currency_detail
from views import currency_cru

currency_urls =[

    url(r'^$',
        currency_detail, name='currency_detail'
    ),
    url(r'^edit/$',
        currency_cru, name='currency_update'
    ),
]