# coding: utf-8

from django.conf.urls import patterns, url
from cms import views

urlpatterns = [
    url(r'^book/$', views.book_list, name='book_list'), #一覧
    url(r'^book/add/$', views.book_edit, name='book_add'), #登録
    url(r'^book/edit/(?P<book_id>\d+)/$', views.book_edit, name='book_edit'), #修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'), #削除
]
