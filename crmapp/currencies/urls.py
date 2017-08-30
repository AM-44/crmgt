from django.conf.urls import url
from views import currency_detail

currency_urls =[

    url(r'^$',
        currency_detail, name='currency_detail'
    ),
]