# Generated by Django 4.1.7 on 2023-02-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0005_alter_task_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="id",
            field=models.PositiveIntegerField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
    ]
