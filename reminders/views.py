from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from cep2015sem2.common.views import *
import datetime
from reminders import models, forms


APP = 'reminders'


class TaskIndexView(BaseListView):
    model = models.Task
    template_name = "task_index.html"
    app = APP
    login_required = True

    def get_queryset(self):
        curruser = get_curruser(self.request.user)
        self.queryset = models.Task.objects.all() if curruser.user.is_superuser else\
            models.Task.objects.filter(owner=curruser)

        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(TaskIndexView, self).get_context_data(**kwargs)
        context['app'] = 'reminders'
        return context


class TaskDetailView(BaseDetailView):
    model = models.Task
    template_name = "task.html"
    context_object_name = 'task'
    app = APP
    login_required = True


class TaskCreateView(BaseCreateView):
    model = models.Task
    form_class = forms.TaskForm
    item_type = "Task"
    super_template = "task_index.html"
    app = APP
    login_required = True
    set_default_user = True


class TaskUpdateView(BaseUpdateView):
    model = models.Task
    form_class = forms.TaskForm
    app = APP
    login_required = True
    set_default_user = True


class TaskDeleteView(BaseDeleteView):
    model = models.Task
    success_url = reverse_lazy('task_index')
    form_class = forms.TagForm
    app = APP
    login_required = True


class TagsCreateView(BaseCreateView):
    model = models.TaskTag
    form_class = forms.TagForm
    item_type = "Tag"
    app = APP
    login_required = True
    set_default_user = True


class TagsUpdateView(BaseUpdateView):
    model = models.TaskTag
    form_class = forms.TagForm
    app = APP
    login_required = True
    set_default_user = True


class TagsDeleteView(BaseDeleteView):
    model = models.TaskTag
    success_url = reverse_lazy('tags_index')
    form_class = forms.TagForm
    app = APP
    login_required = True


class TagsIndexView(BaseListView):
    model = models.TaskTag
    template_name = "tag_index.html"
    login_required = True
    app = APP

    def get_queryset(self):
        curruser = get_curruser(self.request.user)
        self.queryset = models.TaskTag.objects.all() if curruser.user.is_superuser else \
            models.TaskTag.objects.filter(owner=curruser)

        return self.queryset


class TagsDetailView(BaseDetailView):
    login_required = True
    model = models.TaskTag
    template_name = "task_tag.html"
    context_object_name = "tag"
    app = APP
