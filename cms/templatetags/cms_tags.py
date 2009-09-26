from django import template

def snake_cms_url():
    """
    Returns the string contained in the setting SNAKE_CMS_URL.
    """
    try:
        from django.conf import settings
    except ImportError:
        raise template.VariableDoesNotExist('Import error, can not import settings from django.conf.')
        return ''
    if settings.SNAKE_CMS_URL is '':
        raise template.VariableDoesNotExist('Please set the SNAKE_CMS_URL in you settings file.')
    return settings.SNAKE_CMS_URL

def snake_cms_media_url():
    """
    Returns the string contained in the setting SNAKE_CMS_MEDIA_URL.
    """
    try:
        from django.conf import settings
    except ImportError:
        raise template.VariableDoesNotExist('Import error, can not import settings from django.conf.')
        return ''
    if settings.SNAKE_CMS_MEDIA_URL is '':
        raise template.VariableDoesNotExist('Please set the SNAKE_CMS_MEDIA_URL in you settings file.')
    return settings.SNAKE_CMS_MEDIA_URL

register = template.Library()
register.simple_tag(snake_cms_url)
register.simple_tag(snake_cms_media_url)
