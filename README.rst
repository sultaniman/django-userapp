==========================
Django userapp integration
==========================

This is a Django integration with Userapp.io

To use this project you settings should contain

    INSTALLED_APPS = [
        ...
        "django_userapp"
    ]
    
    AUTHENTICATION_BACKENDS = [
        "django_userapp.backends.UserappBackend",
        "django.contrib.auth.backends.ModelBackend"
    ]
    
    USERAPP_ID = "YOUR_USERAPP_ID"


Django version
==============
Django>=1.7

Links
=====
See <http://userapp.io> for full api documentation of Userapp.
