from django import forms
from django.contrib.admin import widgets
from reminders import models


class TagForm(forms.ModelForm):

    class Meta:
        model = models.TaskTag
        fields = '__all__'
        widgets = {
            'owner': forms.HiddenInput(),
            'color_hex': forms.TextInput(attrs={'class': 'colorpicker-child'}),
            'bgc_hex': forms.TextInput(attrs={'class': 'colorpicker-child'}),
        }


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'owner': forms.HiddenInput(),
            'date_end': forms.DateTimeInput(attrs={'class': 'datetimepicker', 'required': True}),
        }
