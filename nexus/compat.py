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
