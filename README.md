### Django userapp integration

This is a Django integration with Userapp.io

To use this project you settings should contain

```py
INSTALLED_APPS = [
    ...
    "django_userapp"
]

AUTHENTICATION_BACKENDS = [
    "django_userapp.backends.UserappBackend",
    "django.contrib.auth.backends.ModelBackend"
]

USERAPP_ID = "YOUR_USERAPP_ID"
USERAPP_USE_FEATURES = True

# if USERAPP_USE_FEATURES = True then 
# checks will happen againts USERAPP_FEATURE.value=true (enabled/disabled)
USERAPP_FEATURES = ["USERAPP_FEATURE"]

# Will be taken when we have not set user email in Userapp
# default untitled@email.com
USERAPP_DEFAULT_EMAIL = "default@email.com"
```

### Note
At Userapp.io you must set first name, last name, email fields for each user.
Emails should be unique and do not intersect with already existing non-userapp emails.

### Django version
Django>=1.7

### Links
See <http://userapp.io> for full api documentation of Userapp.

### TODO

1. Add more tests,
2. Add more readme,
3. Bring more Userapp features,
4. Sync Userapp permissions and features
 