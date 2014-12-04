from django import template
from django.contrib.admin.templatetags import admin_modify

register = template.Library()

@register.inclusion_tag('admin/component_submit_line.html', takes_context=True)
def component_submit_row(context):
    ctx = admin_modify.submit_row(context)
    return ctx
    
