# Generated by Django 4.1.7 on 2023-02-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_task_done"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]