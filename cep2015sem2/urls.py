from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render

import reminders.urls

def main_index(request):
    return render(request, 'home.html', {'webapps': webapps})

urlpatterns = patterns('',
    url(r'^$', main_index, name='main_index'),
    url(r'^admin/', include(admin.site.urls), name='admin_login'),
    url(r'^reminders/', include(reminders.urls.urlpatterns), name='reminders_index'),
)


webapps = [
    ('Django Admin', 'admin/', 'admin_login'),
    ('Reminders', 'reminders/', 'reminders_index')
]