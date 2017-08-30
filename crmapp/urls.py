"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from contacts.urls import contact_urls
from accounts.urls import account_urls
from accounts.views import AccountList
from django.contrib.auth.views import login, logout
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

from marketing.views import HomePage
from subscribers.views import Subscribers
from .settings import LOGIN_REDIRECT_URL
from accounts.views import account_cru
from contacts.views import contact_cru
from contacts.views import ContactDelete
from communications.urls import comm_urls
from communications.views import comm_cru
from communications.views import CommDelete
from currencies.views import CurrencyList

urlpatterns =[

    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$',
        Subscribers, name='sub_new'),

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Login/Logout URLs
    url(r'^login/$',
        login,{'template_name': 'login.html'}, name='django.contrib.auth.views.login'),
    
    url(r'^logout/$',
        logout, {'next_page': '/login/'}
    ),
    
    # Account related URLs
    url(r'^account/new/$',
        account_cru, name='crmapp.accounts.views.account_cru'
    ),
    url(r'^account/new/$',
        account_cru, name='account_new'
    ),
    url(r'^account/list/$',
        AccountList.as_view(), name='account_list'
    ),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
    # Contact related URLS
    url(r'^contact/new/$',
        contact_cru, name='contact_new'
    ),

    url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),
    url(r'^contact/(?P<pk>[\w-]+)/delete/$',
        ContactDelete.as_view(), name='contact_delete'
    ),
    # Communication related URLs
    url(r'^comm/new/$',
        comm_cru, name='comm_new'
    ),
    url(r'^comm/(?P<uuid>[\w-]+)/', include(comm_urls)),
    url(r'^comm/(?P<pk>[\w-]+)/delete/$',
        CommDelete.as_view(), name='comm_delete'
    ),
    # Currency related URLs
    url(r'^currency/list/$',
    CurrencyList.as_view(), name='currency_list'
),
]
