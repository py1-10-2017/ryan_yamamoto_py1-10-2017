from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon/buy/(?P<item_id>\d+)$', views.buy),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^reset$', views.reset)
]
