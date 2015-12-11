import django

# Django <1.9 provides importlib for Python <2.6
try:
    from importlib import import_module  # noqa
except ImportError:
    from django.utils.importlib import import_module  # noqa

# Django <1.9 provides SortedDict on older versions for Python < 2.6
try:
    from collections import OrderedDict  # noqa
except ImportError:
    from django.utils.datastructures import SortedDict as OrderedDict  # noqa

# Django <1.6 provides update_wrapper for Python < 2.6
try:
    from functools import update_wrapper  # noqa
except ImportError:
    from django.utils.functional import update_wrapper  # noqa

# Checks framework only exists on Django 1.7+
try:
    from django.core.checks import Error, Tags, register
except ImportError:
    class CheckMessage(object):
        def __init__(self, level, msg, hint=None, obj=None, id=None):
            self.level = level
            self.msg = msg
            self.hint = hint
            self.obj = obj
            self.id = id

    class Error(CheckMessage):
        def __init__(self, *args, **kwargs):
            super(Error, self).__init__(40, *args, **kwargs)

    Tags = object()

    def register():
        pass

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
