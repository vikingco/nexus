from unittest import skipUnless

import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from django.test.utils import override_settings

from nexus.checks import check_requirements, pre_checks_requirements


class ChecksTests(TestCase):

    @skipUnless(django.VERSION >= (1, 7), "Requires checks framework")
    def test_requirements_pass(self):
        assert check_requirements([]) == []

    @skipUnless(django.VERSION >= (1, 7), "Requires checks framework")
    @override_settings(INSTALLED_APPS=list(set(settings.INSTALLED_APPS) - {'django.contrib.auth'}))
    def test_requirements_fail(self):
        assert len(check_requirements([])) == 1

    @skipUnless(django.VERSION < (1, 7), "Pre-checks framework")
    def test_pre_checks_requirements_pass(self):
        pre_checks_requirements()

    @skipUnless(django.VERSION < (1, 7), "Pre-checks framework")
    @override_settings(INSTALLED_APPS=list(set(settings.INSTALLED_APPS) - {'django.contrib.auth'}))
    def test_pre_checks_requirements_fail(self):
        with self.assertRaises(ImproperlyConfigured):
            pre_checks_requirements()
