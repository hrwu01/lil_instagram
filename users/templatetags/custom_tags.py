import re

from django import template
from django.urls import NoReverseMatch, reverse


register = template.Library()

@register.simple_tag
def is_following(current_user, background_user):
    return background_user.get_followers().filter(creator=current_user).exists()