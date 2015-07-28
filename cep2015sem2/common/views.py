from django.views.generic import CreateView, UpdateView, DeleteView


class BaseCreateView(CreateView):
    template_name = "create_form.html"
    item_type = None


class BaseUpdateView(UpdateView):
    template_name = "update_form.html"
    item_name = None


class BaseDeleteView(DeleteView):
    template_name = "delete_form.html"
    item_name = None
