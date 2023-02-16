from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ("owner",)


class MutateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = (
            "id",
            "done",
            "owner",
        )
