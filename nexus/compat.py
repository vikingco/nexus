# Django provides SortedDict on older versions for Python < 2.6
try:
    from collections import OrderedDict  # noqa
except ImportError:
    from django.utils.datastructures import SortedDict as OrderedDict  # noqa
