from django.conf.urls import url
from views import account_detail
from views import account_cru

account_urls =[

    url(r'^$',
        account_detail, name='account_detail'
    ),
    url(r'^edit/$',
        account_cru, name='account_update'
    ),
]
