# core/templatetags/truncate_filters.py
from django import template
from django.utils.html import strip_tags
register = template.Library()

@register.filter
def truncate_safe(value, arg="160,True"):
    try:
        max_length_str, word_safe_str = arg.split(",")
        max_length = int(max_length_str)
        word_safe = word_safe_str.lower() == "true"
    except Exception:
        max_length = 160
        word_safe = True

    text = strip_tags(value)
    if len(text) > max_length:
        if word_safe:
            return text[:max_length].rsplit(' ', 1)[0] + '...'
        else:
            return text[:max_length] + '...'
    return text
