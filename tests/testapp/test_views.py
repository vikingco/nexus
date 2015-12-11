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
        assert "Model Admin" in resp.content
        assert 'csrftoken' in resp.cookies

    def test_login_not_logged_in(self):
        self.client.logout()
        resp = self.client.get('/nexus/login/')
        assert resp.status_code == 200

    def test_login_do_log_in(self):
        self.client.logout()
        resp = self.client.post('/nexus/login/', data={
            'username': 'user',
            'password': 'password',
        }, follow=False)
        assert resp.status_code == 302
        assert resp['Location'].endswith('/nexus/')

    def test_login_do_log_in_fail(self):
        self.client.logout()
        resp = self.client.post('/nexus/login/', data={
            'username': 'user',
            'password': 'notmypassword',
        }, follow=False)
        assert resp.status_code == 200
        assert '<p class="error"' in resp.content

    def test_login_logged_in(self):
        resp = self.client.get('/nexus/login/', follow=False)
        assert resp.status_code == 302
        assert resp['Location'].endswith('/nexus/')

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
        assert 'Last-Modified' in resp
        assert 'Content-Length' in resp

    def test_media_slash_slash_ignored(self):
        resp = self.client.get('/nexus/media/nexus/img//nexus_logo.png')
        assert resp.status_code == 200

    def test_media_modified_since(self):
        resp = self.client.get('/nexus/media/nexus/img/nexus_logo.png',
                               HTTP_IF_MODIFIED_SINCE='Wed, 25 Feb 2065 17:42:04 GMT')
        assert resp.status_code == 304

    def test_media_non_existent(self):
        resp = self.client.get('/nexus/media/nexus/img/doesnotexist.png')
        assert resp.status_code == 404

    def test_media_directory_not_allowed(self):
        resp = self.client.get('/nexus/media/nexus/img/doesnotexist.png')
        assert resp.status_code == 404
