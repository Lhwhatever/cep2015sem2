from django.template.loader_tags import register


@register.filter
def fieldtype(obj):
    return obj.__class__.__name__
