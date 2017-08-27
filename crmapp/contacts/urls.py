from django.conf.urls import url
from views import contact_detail
from views import contact_cru

contact_urls = [

    url(r'^$', contact_detail, name="contact_detail"),

    url(r'^edit/$',
        contact_cru, name='contact_update'
    ),
]
