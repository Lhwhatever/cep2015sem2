from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from django.views.generic import *
import accounts.urls
from cep2015sem2.common.views import get_curruser
import reminders.urls


class MainIndexView(TemplateView):

    template_name = 'home.html'
    extra_context = {
        'webapps': [('Reminders', 'task_index')],
    }

    def get_context_data(self, **kwargs):
        return super(MainIndexView, self).get_context_data(message=self.request.session.pop('message', None),
                                                           app='home', curruser=get_curruser(self.request.user),
                                                           **self.extra_context)


urlpatterns = patterns('',
    url(r'^$', MainIndexView.as_view(), name='main_index'),
    url(r'^accounts/', include(accounts.urls.urlpatterns)),
    url(r'^admin/', include(admin.site.urls), name='admin_login'),
    url(r'^reminders/', include(reminders.urls.urlpatterns)),
)

