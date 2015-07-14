from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from random import randrange
from django.views.generic import *

import reminders.urls

class MainIndexView(View):
    webapps = [
        ('Django Admin', 'admin:index'),
        ('Reminders', 'task_index')
    ]

    def get(self, request):
        return render(request, 'home.html', {'webapps': MainIndexView.webapps})

urlpatterns = patterns('',
    url(r'^$', MainIndexView.as_view(), name='main_index'),
    url(r'^admin/', include(admin.site.urls), name='admin_login'),
    url(r'^reminders/', include(reminders.urls.urlpatterns)),
)

