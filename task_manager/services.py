# -*- coding: utf-8 -*-
import time
import uuid

from django_extra.core.services import BaseService

from .models import Task
from .serializers import TaskSerializer


class TaskService(BaseService):
    serializer = TaskSerializer
    model = Task

    def create(self, data):
        if not data.get("identifier"):
            data["identifier"] = str(uuid.uuid4())
        data["created_at"] = int(time.time())
        return super().create(data)

    def update(self, data, partial=True):
        data["updated_at"] = int(time.time())
        return super().update(data, partial)
