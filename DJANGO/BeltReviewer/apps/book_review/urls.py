from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^add_book$', views.add_book),
    url(r'^post_book$', views.post_book),
    url(r'^book/(?P<book_id>\d+)$', views.show_book),
    url(r'^book/(?P<book_id>\d+)/create$', views.create),
    url(r'^user/(?P<user_id>\d+)$', views.show_user),
    url(r'^book/delete/(?P<review_id>\d+)$', views.delete_review),
]
