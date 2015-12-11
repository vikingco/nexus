import django

# context_processors moved in Django 1.8
try:
    from django.template import context_processors  # noqa
except ImportError:
    from django.core import context_processors  # noqa


# 'dictionary' -> 'context' in Django 1.8
if django.VERSION[:2] >= (1, 8):
    from django.shortcuts import render
    from django.template.loader import render_to_string
else:
    from django.shortcuts import render as orig_render
    from django.template import RequestContext
    from django.template.loader import render_to_string as orig_render_to_string

    def render(*args, **kwargs):
        if 'context' in kwargs:
            kwargs['dictionary'] = kwargs.pop('context')
        return orig_render(*args, **kwargs)

    def render_to_string(*args, **kwargs):
        if 'context' in kwargs:
            kwargs['dictionary'] = kwargs.pop('context')
        if 'request' in kwargs:
            kwargs['context_instance'] = RequestContext(kwargs.pop('request'))
        return orig_render_to_string(*args, **kwargs)
