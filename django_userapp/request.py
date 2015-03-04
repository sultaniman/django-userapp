# -*- coding: utf-8 -*-
import userapp
from django.conf import settings


userapp_api = userapp.API(app_id=settings.USERAPP_ID)


def get_user(session):
    """ Returns userapp user object """
    token = session.get("userapp_token", None)

    try:
        userapp_api.set_option("token", token)
        users = userapp_api.user.get(user_id="self")

        if users:
            return users[0]
    except userapp.UserAppServiceException as e:
        if e.error_code in {"USER_NOT_AUTHORIZED", "INVALID_CREDENTIALS"}:
            return None


def login(request, username=None, password=None):
    """ Authenticates Userapp user and return result """

    try:
        userapp_api.set_option("token", "")
        result = userapp_api.user.login(login=username, password=password)
        request.session["userapp_token"] = result["token"]
        return userapp_api.user.get(user_id="self")
    except userapp.UserAppServiceException:
        return None
