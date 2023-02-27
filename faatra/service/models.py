from pyexpat import model
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



class Files(models.Model):
    document = models.FileField(upload_to='doc/')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='files')

    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"