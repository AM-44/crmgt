from django.conf.urls import url
from views import comm_detail

comm_urls = [

    url(r'^$',
        comm_detail, name="comm_detail"
    ),

]
