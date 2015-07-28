from django.conf.urls import patterns, include, url
from django.contrib import admin
from reminders import views


urlpatterns = patterns(
    '',

    # Task Index - Simple
    url(r'^$', views.TaskIndexView.as_view()),
    url(r'^task/$', views.TaskIndexView.as_view(), name='task_index'),
    url(r'^task/create/$', views.TaskCreateView.as_view(), name='task_create'),
    url(r'^task/(?P<pk>\d+)/+$', views.TaskDetailView.as_view(), name='task_detail'),
    url(r'^task/(?P<pk>\d+)/update/+$', views.TaskUpdateView.as_view(), name='task_update'),
    url(r'^task/(?P<pk>\d+)/delete/+$', views.TaskDeleteView.as_view(), name='task_delete'),

    url(r'^tags/$', views.TagsIndexView.as_view(), name='tags_index'),
    url(r'^tags/create/$', views.TagsCreateView.as_view(), name='tags_create'),
    url(r'^tags/(?P<pk>\d+)/+$', views.TagsDetailView.as_view(), name='tags_detail'),
    url(r'^tags/(?P<pk>\d+)/update/+$', views.TagsUpdateView.as_view(), name='tags_update'),
    url(r'^tags/(?P<pk>\d+)/delete/+$', views.TagsDeleteView.as_view(), name='tags_delete')
)