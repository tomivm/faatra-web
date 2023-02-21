from django.db import models
from django_quill.fields import QuillField
from saloon.models import Saloon
from shared.models import BaseTextModel

# Create your models here.


class OfferCategory(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=256)
    icon = models.FileField(
        upload_to="media/", verbose_name="Imagen", blank=True, null=True
    )
    image_backgroud = models.FileField(
        upload_to="media/", verbose_name="Imagen de fondo", blank=True, null=True
    )
    is_available = models.BooleanField(verbose_name="Habilitado", default=False)

    class Meta:
        verbose_name = "Categoria de oferta"
        verbose_name_plural = "Categorias de ofertas"

    def __str__(self):
        return f"{self.title}"


class Topic(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=256)
    is_available = models.BooleanField(verbose_name="Habilitado", default=False)

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"

    def __str__(self):
        return f"{self.title}"



class Mode(models.Model):
    description = models.CharField(verbose_name="Modalidad", max_length=256)

    class Meta:
        verbose_name = "Modalidad"
        verbose_name_plural = "Modalidades"

    def __str__(self):
        return f"{self.description}"

class InformativeOffer(BaseTextModel):
    email_info = QuillField()
    saloon = models.ForeignKey(Saloon, verbose_name="Camara", on_delete=models.CASCADE)
    category = models.ForeignKey(
        OfferCategory, verbose_name="Categoria", on_delete=models.CASCADE
    )
    city = models.CharField("Ciudad", max_length=512, blank=True, null=True)
    duration = models.CharField("Duracion", max_length=512, blank=True, null=True)
    topic = models.ForeignKey(Topic, verbose_name="Tema", on_delete=models.CASCADE)
    enable_inscription = models.BooleanField("Habilitar inscripción", default=False)
    exhausted = models.BooleanField("Agotado", default=False)
    cancelled = models.BooleanField("Cancelado", default=False)
    due_date = models.DateField("Fecha cuando se cierra la inscripcion")
    use_in_home = models.BooleanField("Usar en la pagina principal", default=False)
    mode = models.ForeignKey(Mode, verbose_name="Modalida", on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(
        upload_to="media/", verbose_name="Imagen", null=False
    )
    banner_background_image = models.ImageField(
        upload_to="media/", verbose_name="Banner Home (1300x480px)", blank=True, null=True
    )

    class Meta:
        verbose_name = "Oferta formativa"
        verbose_name_plural = "Oferta formativa"

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if self.use_in_home:
            InformativeOffer.objects.filter(use_in_home=True).exclude(id=self.id).update(use_in_home=False)
        return super().save(*args, **kwargs)


class DateRealization(models.Model):
    created_date = models.DateField(
        verbose_name="Fecha de creación",
    )
    hours = models.CharField(verbose_name="Hora", max_length=256)
    offer = models.ForeignKey(
        InformativeOffer, verbose_name="Oferta formativa", on_delete=models.CASCADE, related_name="dates"
    )

    class Meta:
        verbose_name = "Fecha de realizacion"
        verbose_name_plural = "Fechas de realizacion"
