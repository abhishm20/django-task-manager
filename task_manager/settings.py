# -*- coding: utf-8 -*-
from django.conf import settings

# pylint: disable=invalid-name

INSTALLED_APPS = ["task_manager"]


class AppSettings:
    def __init__(self):
        self.app_settings = getattr(settings, "DJANGO_EXTRA_SETTINGS", {})

    @property
    def SERVICE_NAME(self):
        """Control how many times a task will be attempted."""
        return getattr(self.app_settings, "SERVICE_NAME", "task_manager")

    @property
    def USE_SERVICE_CACHE(self):
        return getattr(self.app_settings, "USE_SERVICE_CACHE", False)


app_settings = AppSettings()
