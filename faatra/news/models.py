from django.db import models
from training.models import InformativeOffer
from saloon.models import Saloon
import datetime

from shared.models import BaseTextModel


# Create your models here.


class Video(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=256)
    video = models.CharField(verbose_name="video", max_length=256)
    is_available = models.BooleanField(verbose_name="Habilitado", default=False)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return f"{self.title}"


class New(BaseTextModel):
    saloon = models.ForeignKey(
        Saloon, verbose_name="Camara", on_delete=models.CASCADE, blank=True, null=True
    )
    course = models.ForeignKey(
        InformativeOffer,
        verbose_name="Curso",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    use_in_home = models.BooleanField("Usar en la pagina principal", default=False)

    banner_background_image = models.ImageField(
        upload_to="media/", verbose_name="Banner Home (1300x480px)", blank=True, null=True
    )

    created_date = models.DateTimeField(
        verbose_name="Fecha de creación",
        auto_created=False,
    )

    class Meta:
        verbose_name = "Novedades"
        verbose_name_plural = "Novedades"

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if self.use_in_home:
            New.objects.filter(use_in_home=True).exclude(id=self.id).update(use_in_home=False)
        return super().save(*args, **kwargs)
