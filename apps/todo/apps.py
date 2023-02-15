from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.todo"

    def ready(self) -> None:
        import apps.todo.signals
