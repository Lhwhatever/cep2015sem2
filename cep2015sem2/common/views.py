from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, View, DetailView
from accounts.models import UserProfile


def get_curruser(user):
    return UserProfile.objects.get(user=user) if user.is_authenticated() else None


class BaseListView(ListView):

    app = 'home'
    login_required = False

    def get_context_data(self, **kwargs):
        return super(BaseListView, self).get_context_data(curruser=get_curruser(self.request.user),
                                                          app=self.app,
                                                          message=self.request.session.pop('message', None), **kwargs)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(BaseListView, self).dispatch, enforce=self.login_required)


class BaseDetailView(DetailView):
    app = 'home'
    login_required = False

    def get_context_data(self, **kwargs):
        return super(BaseDetailView, self).get_context_data(curruser=get_curruser(self.request.user),
                                                            app=self.app,
                                                            message=self.request.session.pop('message', None), **kwargs)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(BaseDetailView, self).dispatch, enforce=self.login_required)


class BaseCreateView(CreateView):
    template_name = "create_form.html"
    item_type = None
    login_required = False
    set_default_user = False
    app = 'home'

    def get_context_data(self, **kwargs):
        return super(BaseCreateView, self).get_context_data(curruser=get_curruser(self.request.user),
                                                            app=self.app,
                                                            message=self.request.session.pop('message', None), **kwargs)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(BaseCreateView, self).dispatch, enforce=self.login_required,
                                       blacklist=(not self.object.private), users=(self.object.owner,))

    def get_initial(self):
        initial = super(BaseCreateView, self).get_initial().copy()
        if self.set_default_user:
            initial['owner'] = get_curruser(self.request.user)
        return initial


class BaseUpdateView(UpdateView):
    template_name = "update_form.html"
    item_name = None
    app = 'home'
    set_default_user = False
    login_required = False

    def get_context_data(self, **kwargs):
        return super(BaseUpdateView, self).get_context_data(curruser=get_curruser(self.request.user),
                                                            app=self.app,
                                                            message=self.request.session.pop('message', None), **kwargs)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(BaseUpdateView, self).dispatch, enforce=self.login_required)

    def get_initial(self):
        initial = super(BaseUpdateView, self).get_initial()
        if self.set_default_user:
            initial['owner'] = get_curruser(self.request.user)
        return initial


class BaseDeleteView(DeleteView):
    template_name = "delete_form.html"
    item_name = None
    login_required = False
    app = 'home'
    set_default_user = False

    def get_context_data(self, **kwargs):
        return super(BaseDeleteView, self).get_context_data(curruser=get_curruser(self.request.user),
                                                            app=self.app,
                                                            message=self.request.session.pop('message', None), **kwargs)

    def dispatch(self, request, *args, **kwargs):
        return login_required_redirect(request, super(BaseDeleteView, self).dispatch, enforce=self.login_required)


def redirect_with_message(request, message, to, permanent=False, *args, **kwargs):
    request.session['message'] = message
    return redirect(to, permanent=permanent, *args, **kwargs)


def login_required_redirect(request, dispatch, message=None, redirect_to=None, enforce=True,
                            users=None, blacklist=True, *args, **kwargs):
    if (not enforce) or request.user.is_authenticated():
        if (get_curruser(request.user) in (users or tuple())) ^ blacklist:
            return dispatch(request, *args, **kwargs)
        else:
            return redirect_with_message(request,
                                         message or 'This page is private.',
                                         redirect_to or settings.LOGIN_URL,
                                         *args, **kwargs)
    else:
        return redirect_with_message(request,
                                     message or 'You need to log in to see this page.',
                                     redirect_to or settings.LOGIN_URL,
                                     *args, **kwargs)
