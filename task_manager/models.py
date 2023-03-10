# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import JSONField
from django_extra.core.models import AbstractModel

from .constants import TaskStatus


class Task(AbstractModel):
    id = models.CharField(unique=True, primary_key=True, max_length=36)
    identifier = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20, default=TaskStatus.PENDING, choices=TaskStatus.choices
    )
    args = JSONField(blank=True, null=True)
    kwargs = JSONField(blank=True, null=True)
    return_value = models.TextField(blank=True, null=True)
    failed_reason = models.TextField(blank=True, null=True)
    counter = models.IntegerField(default=1)

    created_at = models.CharField(max_length=32, null=True, default=None)
    updated_at = models.CharField(max_length=32, null=True, default=None)
