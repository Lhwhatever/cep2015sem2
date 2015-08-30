from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns(
    '',
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^relog/$', views.RelogView.as_view(), name='relog'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
)
