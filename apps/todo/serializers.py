from rest_framework import serializers
from .models import Task


class CreateOrUpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = (
            "id",
            "done",
            "owner",
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta(CreateOrUpdateTaskSerializer.Meta):
        exclude = ("owner",)
