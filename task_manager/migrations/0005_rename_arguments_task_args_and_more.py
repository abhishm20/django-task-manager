# -*- coding: utf-8 -*-
# Generated by Django 4.1.6 on 2023-02-09 01:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0004_alter_task_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="arguments",
            new_name="args",
        ),
        migrations.RenameField(
            model_name="task",
            old_name="keyword_argument",
            new_name="kwargs",
        ),
    ]
