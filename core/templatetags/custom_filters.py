from django import template

register = template.Library()

@register.filter
def startswith(text, starts):
    """
    Проверяет, начинается ли строка с указанного префикса
    """
    if isinstance(text, str):
        return text.startswith(starts)
    return False