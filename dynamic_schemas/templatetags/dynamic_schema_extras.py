from django import template
from django.contrib.auth.models import User

import json
import ast

register = template.Library()

@register.filter
def is_a_checkbox(field):
    if field.subwidgets[0].data['type'] == 'checkbox':
        return True
    return False 

@register.filter
def load_json(data):
    eval_json = ast.literal_eval(data)
    return eval_json.items()

@register.filter
def get_full_user_name(user_id):
    username = User.objects.get(pk=user_id).username
    full_name = User.objects.get(pk=user_id).get_full_name()

    if full_name != '':
        return full_name
    else:
        return username

