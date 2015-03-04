# -*- coding: utf-8 -*-
import os
import mock
import json

from django.test import TestCase
from django.contrib.auth import get_user_model

from django_userapp.backends import UserappBackend
from django_userapp.request import login


User = get_user_model()

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
LOGIN_MOCK = "django_userapp.request.login"
USERAPP_LOGIN_MOCK = "django_userapp.request.userapp_api.user.login"
USER_MOCK = "django_userapp.request.userapp_api.user.get"
CONF_MOCK = "django_userapp.request.settings"
FAKE_RESULT = open(os.path.join(CURRENT_DIR, "userapp_fake_result.json"), "r").read()
FAKE_USER = open(os.path.join(CURRENT_DIR, "userapp_sample_response.json"), "r").read()


class Dummy(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TestDjangoUserapp(TestCase):
    """ Test django-userapp integration """

    def setUp(self):
        # note we don't have to store user passwords
        # so just set some dummy password
        self.user, self.created = User.objects.get_or_create(username="username", 
                                                             password="password")
        self.ua_result = json.loads(FAKE_RESULT)
        self.ua_user = json.loads(FAKE_USER)
        self.request = Dummy(**{"session": {}})

    def test_user_created(self):
        """ Test user creation / just warming up """
        self.assertTrue(self.created)

    @mock.patch(LOGIN_MOCK)
    @mock.patch(USERAPP_LOGIN_MOCK)
    @mock.patch(USER_MOCK)
    def test_userapp_api(self, get_user, userapp_login, our_login):
        userapp_login.return_value = self.ua_result
        our_login.return_value = self.ua_result
        result = login(self.request, username=self.user.username, password=self.user.password)
        self.assertEqual(result, FAKE_RESULT)

    @mock.patch.object(UserappBackend, "authenticate")
    def test_userapp_auth(self, mock_auth):
        pass
