from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "butter_exercise.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import butter_exercise.users.signals  # noqa F401
        except ImportError:
            pass
