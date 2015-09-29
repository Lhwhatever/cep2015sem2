import json
from django.contrib import auth
from django.contrib.auth import views, authenticate, login
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse_lazy, reverse
from django.forms.utils import ErrorDict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from accounts import forms
from accounts.models import UserProfile
from cep2015sem2 import common
from cep2015sem2.common.views import login_required_redirect, redirect_with_message, BaseDetailView, get_curruser


class LoginView(generic.FormView):
    template_name = 'login.html'
    app = 'home'

    def dispatch(self, request, *args, **kwargs):

        return redirect_with_message(request, 'You are already logged in.', 'main_index') if\
            request.user.is_authenticated() else views.login(request, extra_context=self.get_context_data(), **kwargs)

    def get_context_data(self, **kwargs):
        return super(LoginView, self).get_context_data(app=self.app, **kwargs)


class LogoutView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        request.session['message'] = 'Logged out successfully.' if request.user.is_authenticated()\
            else None

        return views.logout(request, next_page='/') if request.user.is_authenticated()\
            else redirect_with_message(request, 'You are already logged out.', 'main_index')


class RelogView(generic.View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return views.logout_then_login(request, *args, **kwargs)
        else:
            return views.login(request, *args, **kwargs)


class RegisterView(generic.TemplateView):
    template_name = 'registration/register.html'
    app = 'home'

    user_form = forms.UserForm
    profile_form = forms.UserProfileForm

    def get(self, request, *args, **kwargs):
        kwargs.setdefault('user_form', self.user_form())
        kwargs.setdefault('profile_form', self.profile_form())
        return super(RegisterView, self).get(request, *args, app='home', **kwargs)

    def post(self, request, *args, **kwargs):
        user_form = self.user_form(data=request.POST)
        profile_form = self.profile_form(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            user = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password1'))
            login(request, user)
            return redirect_with_message(request, 'Welcome!', 'main_index')

        else:
            return redirect_with_message(
                request, 'The following errors were found: \n{0} \n{1}'.format(user_form.errors, profile_form.errors),
                'register'
            )


class ProfileView(generic.TemplateView):

    template_name = 'profile.html'
    user_form = forms.UserUpdateForm
    profile_form = forms.UserProfileForm
    password_form = forms.ChangePasswordForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            kwargs.setdefault('user_form', self.user_form(initial={'username': request.user.username,
                                                                   'email': request.user.email}))
            kwargs.setdefault('profile_form', self.profile_form(
                initial={'about_me': get_curruser(request.user).about_me}
            ))
            kwargs.setdefault('password_form', self.password_form())
            return super(ProfileView, self).get(request, *args, **kwargs)
        else:
            return redirect_with_message(request, 'You need to be logged in to do this.', '/')

    def post(self, request, *args, **kwargs):
        print(request.POST)

        response_dict = {}

        if request.POST.get('form_key') == 'edit_profile':
            form_a = self.user_form(pk=request.user.pk, data=request.POST)
            form_b = self.profile_form(user=request.user, data=request.POST)

            errors = ErrorDict()
            if form_a.errors:
                errors.update(form_a.errors)

            if form_b.errors:
                errors.update(form_b.errors)

            if not (form_a.is_valid() and form_b.is_valid()):
                response_dict.update({
                    'status': 0,
                    'message': errors.as_ul()
                })

            elif authenticate(username=request.user.username, password=request.POST.get('password')):
                u1 = form_a.save()
                u2 = form_b.save()

                response_dict.update({
                    'status': 1,
                    'message': 'User was successfully updated.',
                    'instance': {
                        'username': u1.username,
                        'email': u1.email,
                        'about_me': u2.about_me,
                    }
                })
            else:
                response_dict.update({
                    'status': 0,
                    'message': 'Password is incorrect.'
                })

            return HttpResponse(json.dumps(response_dict, cls=DjangoJSONEncoder))

        elif request.POST.get('form_key') == 'change_pw':
            form = self.password_form(pk=request.user.pk, data=request.POST)

            if not form.is_valid():
                response_dict.update({
                    'status': 0,
                    'message': form.errors.as_ul()
                })
            elif authenticate(username=request.user.username, password=request.POST.get('old_password')):
                form.save()
                response_dict.update({
                    'status': 1,
                    'message': 'Password was successfully updated.'
                })
            else:
                response_dict.update({
                    'status': 0,
                    'message': 'Old password is incorrect.'
                })

            return HttpResponse(json.dumps(response_dict, cls=DjangoJSONEncoder))
        return super(ProfileView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(ProfileView, self).get_context_data(message=self.request.session.pop('message', None),
                                                         app='home', curruser=get_curruser(self.request.user), **kwargs)

