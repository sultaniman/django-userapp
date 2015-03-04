# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from .request import login

import re


UserModel = get_user_model()


class UserappBackend(object):
    def authenticate(self, username=None, password=None, request=None, **kwargs):
        result = login(request, username=username, password=password)

        try:
            if result is None:
                raise UserModel.DoesNotExist("Userapp account not found")

            user = result[0]
            our_username = re.sub(r"[@\.\-]", "_", username)
            our_user, created = UserModel.objects.get_or_create(username=our_username[0:29],
                                                                email=user["email"])

            return our_user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
