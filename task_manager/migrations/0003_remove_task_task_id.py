# -*- coding: utf-8 -*-
# Generated by Django 4.1.6 on 2023-02-09 00:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0002_alter_task_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="task_id",
        ),
    ]