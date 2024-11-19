from django.apps import AppConfig
from django.core.checks import register
from django.utils.translation import gettext_lazy as _

from django_removals.checks.settings import check_removed_settings


class DjangoRemovalsConfig(AppConfig):
    name = "django_removals"
    verbose_name = _("Django Removals")

    def ready(self):
        register(check_removed_settings)
