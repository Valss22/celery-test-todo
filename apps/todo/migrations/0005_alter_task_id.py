# Generated by Django 4.1.7 on 2023-02-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0004_alter_task_period_of_execution"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="id",
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]