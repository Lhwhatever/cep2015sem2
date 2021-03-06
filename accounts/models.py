from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    about_me = models.TextField("About Me")

    def __str__(self):
        return self.user.username
