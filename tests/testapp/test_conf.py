from django.test import SimpleTestCase
from django.test.utils import override_settings

from nexus.conf import nexus_settings


class NexusSettingsTests(SimpleTestCase):

    @override_settings(NEXUS_MEDIA_PREFIX='/mynexusprefix/')
    def test_with_override_settings(self):
        self.assertEqual(nexus_settings.MEDIA_PREFIX, '/mynexusprefix/')
