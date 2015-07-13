from django.conf.urls import patterns, include, url
from django.contrib import admin
from reminders import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^task/$', views.index, name='task_index'),
    url(r'^task/(?P<task_id>\d+)/+$', views.task_detail, name='task_detail')
)