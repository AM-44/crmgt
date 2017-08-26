from django.conf.urls import patterns, url

contact_urls = [

    url(r'^$', 'crmapp.contacts.views.contact_detail', name="contact_detail"),

]
