# -*- coding: utf-8 -*-
import os
import mock
import json

from django.test import TestCase
from django.contrib.auth import get_user_model

from django_userapp.backends import UserappBackend
from django_userapp import request
from django_userapp.request import userapp_api


User = get_user_model()
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
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


    @mock.patch.object(UserappBackend, "authenticate")
    @mock.patch("django_userapp.request.login")
    @mock.patch("django_userapp.request.userapp_api.user.login")
    @mock.patch("django_userapp.request.userapp_api.user")
    def test_userapp_api(self, ua_user, ua_login, our_login, backend):
        ua_login.return_value = self.ua_result
        backend.return_value = self.ua_user
        our_login.login.return_value = self.ua_user
        ua_user.get.return_value = self.ua_user

        userapp_backend = UserappBackend()
        result = userapp_backend.authenticate(username=self.user.username,
                                              password=self.user.password,
                                              request=self.request)

        request.login(request=self.request,
                      username=self.user.username,
                      password=self.user.password)

        userapp_result = userapp_api.user.login(login=self.user.username,
                                                password=self.user.password)

        backend.assert_called_with(username=self.user.username,
                                   password=self.user.password,
                                   request=self.request)

        our_login.assert_called_with(username=self.user.username,
                                     password=self.user.password,
                                     request=self.request)

        ua_login.assert_called_with(login=self.user.username,
                                    password=self.user.password)

        self.assertEqual(result, self.ua_user)
        self.assertEqual(userapp_result, self.ua_result)
