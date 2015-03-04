# -*- coding: utf-8 -*-
import os
import sys

from django.conf import settings


test_settings = {
    "DATABASES": {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    
    "INSTALLED_APPS": [
        "django.contrib.auth",
        "django.contrib.sessions",
        "django_userapp",
        "test_app"
    ],

    "USERAPP_ID": "FAKE_USERAPP_ID",

    "AUTHENTICATION_BACKENDS": [
        "django_userapp.backends.UserappBackend",
        "django.contrib.auth.backends.ModelBackend"
    ],
    
    "MIDDLEWARE_CLASSES": [
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware"
    ],
    
    "ROOT_URLCONF": "test_app.urls"
}


if __name__ == "__main__":
    from django.test.simple import DjangoTestSuiteRunner

    current_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    sys.path.insert(0, current_path)
    sys.path.insert(0, os.path.join(current_path, "tests"))
    settings.configure(**test_settings)

    runner = DjangoTestSuiteRunner(verbosity=2, interactive=True, failfast=False)
    failures = runner.run_tests(["test_app"])

    sys.exit(failures)
