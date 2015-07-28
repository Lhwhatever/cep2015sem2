from django import forms
from django.contrib.admin import widgets
from reminders import models


class TagForm(forms.ModelForm):

    class Meta:
        model = models.TaskTag
        fields = '__all__'
        widgets = {
            'color_hex': forms.TextInput(attrs={'class': 'colorpicker-child'}),
            'bgc_hex': forms.TextInput(attrs={'class': 'colorpicker-child'}),
        }


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'date_end': forms.DateTimeInput(attrs={'class': 'datetimepicker', 'required': True}),
        }
