from django.contrib.auth.models import User
from django.test import TestCase


class ViewTests(TestCase):

    def setUp(self):
        self.user = User(username='user', is_staff=True)
        self.user.set_password('password')
        self.user.save()
        self.client.login(username='user', password='password')

    def test_dashboard_not_logged_in(self):
        self.client.logout()
        resp = self.client.get('/nexus/')
        assert resp.status_code == 200
        assert "You must log in to continue" in resp.content

    def test_dashboard_logged_in(self):
        resp = self.client.get('/nexus/')
        assert resp.status_code == 200
        print resp.content
        assert "Model Admin" in resp.content

    def test_logout_not_logged_in(self):
        self.client.logout()
        resp = self.client.get('/nexus/logout/')
        assert resp.status_code == 200
        assert "You must log in to continue" in resp.content

    def test_logout_logged_in(self):
        resp = self.client.get('/nexus/logout/', follow=False)
        assert resp.status_code == 302
        assert resp['Location'].endswith('/nexus/')

    def test_media_logo(self):
        resp = self.client.get('/nexus/media/nexus/img/nexus_logo.png')
        assert resp.status_code == 200
