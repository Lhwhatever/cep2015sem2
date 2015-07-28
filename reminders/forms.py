from django import forms
from django.contrib.admin import widgets
from reminders import models


class TagForm(forms.ModelForm):

    class Meta:
        model = models.TaskTag
        fields = '__all__'
        widgets = {
            'color_hex': forms.TextInput(attrs={'type': 'color'}),
            'bgc_hex': forms.TextInput(attrs={'type': 'color'}),
        }


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'date_end': forms.DateTimeInput(attrs={'class': 'datetimepicker', 'required': True}),
        }
