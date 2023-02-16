from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, MutateTaskSerializer
from .celery_tasks import send_email_task


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return MutateTaskSerializer
        return TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(["POST"])
def execute_task(request: Request, id: int):
    done: bool | None = request.data.get("done")

    if done is not None:
        try:
            task = Task.objects.get(id=id, owner=request.user)
            task.done = done
            task.save()
            send_email_task.apply_async(
                args=(
                    "Task",
                    f"Your task {task.title} is done = {done}",
                    [request.user.profile.email],
                ),
                queue="email",
            )

            return Response({"detail": "Task is executed"}, status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({"detail": "Task not found"}, status.HTTP_204_NO_CONTENT)

    return Response({"detail": "done is required"}, status.HTTP_200_OK)
