# -*- coding: utf-8 -*-
# Generated by Django 4.1.6 on 2023-02-09 01:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0005_rename_arguments_task_args_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="exception",
        ),
        migrations.AddField(
            model_name="task",
            name="failed_reason",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="return_value",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("running", "Running"),
                    ("success", "Success"),
                    ("failed", "Failed"),
                    ("retrying", "Retrying"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
