from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value, arg):
    """
    This function remove all value  of 'arg' from the given string
    """
    return value.replace(arg, '')