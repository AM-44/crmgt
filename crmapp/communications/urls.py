from django.conf.urls import url
from views import comm_detail
from views import comm_cru

comm_urls = [

    url(r'^$',
        comm_detail, name="comm_detail"
    ),
    url(r'^edit/$',
        comm_cru, name='comm_update'
    ),
]
