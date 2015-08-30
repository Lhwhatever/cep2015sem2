from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, PasswordInput, CharField, HiddenInput, save_instance
from accounts.models import UserProfile
from cep2015sem2.common.views import get_curruser


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('about_me',)

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(UserProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = False
        return self.cleaned_data

    def save(self, commit=True):
        u = get_curruser(self.user)
        u.about_me = self.cleaned_data.get('about_me')
        u.save()

        return u


class UserUpdateForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, pk=None, *args, **kwargs):
        self.pk = pk
        super(UserUpdateForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(UserUpdateForm, self).is_valid()

    def clean(self):
        self._validate_unique = False
        return self.cleaned_data

    def save(self, commit=True):

        u = User.objects.get(pk=self.pk)
        u.username = self.cleaned_data.get('username')
        u.email = self.cleaned_data.get('email')
        u.save()

        return u


class ChangePasswordForm(Form):
    old_password = CharField(widget=PasswordInput(), label="Old Password")
    password1 = CharField(widget=PasswordInput(), label="New Password")
    password2 = CharField(widget=PasswordInput(), label="Confirm New Password")

    def __init__(self, pk=None, *args, **kwargs):
        self.pk = pk
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        if not(cleaned_data.get('password1') == cleaned_data.get('password2')):
            self.add_error('password2', "New passwords do not match.")
        elif cleaned_data.get('old_password') is cleaned_data.get('password1'):
            self.add_error('password1', "No change in passwords.")

        return cleaned_data

    class Meta:
        fields = '__all__'

    def save(self):
        u = User.objects.get(pk=self.pk)
        u.set_password(self.cleaned_data.get('password1'))
        u.save()
        return u
    
    def is_valid(self):
        return self.is_bound and not self.errors
