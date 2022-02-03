from django.db import models

from shared.models import BaseTextModel

# Create your models here.


class Service(BaseTextModel):
    icon = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self) -> str:
        return self.title
