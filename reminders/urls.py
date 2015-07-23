from django.conf.urls import patterns, include, url
from django.contrib import admin
from reminders import views


urlpatterns = patterns(
    '',

    # Task Index - Simple
    url(r'^$', views.TaskIndexView.as_view()),
    url(r'^task/$', views.TaskIndexView.as_view(), name='task_index'),

    #url(r'^task/(o/(?P<order>\w+)/)?(f/(?P<filter>\w+)/)?(?P<reverse>reverse)?$',
    #    views.TaskIndexView.as_view(), name='task_index'),

    # Task Detail View
    url(r'^task/(?P<pk>\d+)/+$', views.TaskDetailView.as_view(), name='task_detail'),

    url(r'^tags/$', views.TagsIndexView.as_view(), name='tags_index'),
    url(r'^tags/(?P<pk>\d+)/+$', views.TagsDetailView.as_view(), name='tags_detail'),
)