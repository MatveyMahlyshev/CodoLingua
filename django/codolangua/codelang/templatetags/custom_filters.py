from django import template

register = template.Library()

@register.filter
def get_next_code(code_list, current_index):
    try:
        next_index = current_index
        return code_list[next_index - 1]
    except IndexError:
        return None