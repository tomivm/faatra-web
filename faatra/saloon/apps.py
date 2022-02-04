from tabnanny import verbose
from django.apps import AppConfig


class SaloonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "saloon"
    verbose_name = "Contenidos"
