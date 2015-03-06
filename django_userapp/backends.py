# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.conf import settings

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
            default_email = getattr(settings, "USERAPP_DEFAULT_EMAIL", "untitled@email.com")

            if self.passes_checks(user):
                email = getattr(user, "email", default=default_email)
                our_username = re.sub(r"[@\.\-]", "_", username)
                our_user, created = UserModel.objects.get_or_create(email__exact=email)

                if created:     # If user is new user then set username
                    our_user.username = our_username[0:29]
                    our_user.email = email
                    our_user.save()

                if not our_user.password:       # Means that user was created by our backend
                    return our_user

                return None
            else:
                return None
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

    def passes_checks(self, user):
        """ Basically checks features and if finds any match returns True """
        user_features = {}
        features = getattr(settings, "USERAPP_FEATURES", [])
        use_features = getattr(settings, "USERAPP_USE_FEATURES", False)

        if "features" in user:
            user_features = user["features"]

        if use_features is False:
            return True

        for feature in features:
            if feature in user_features and user_features[feature]["value"]:
                return True

        return False
