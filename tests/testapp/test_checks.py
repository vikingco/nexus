from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings

from nexus.checks import check_requirements


class ChecksTests(TestCase):

    def test_requirements_pass(self):
        assert check_requirements([]) == []

    @override_settings(INSTALLED_APPS=list(set(settings.INSTALLED_APPS) - {'django.contrib.auth'}))
    def test_requirements_fail(self):
        assert len(check_requirements([])) == 1
