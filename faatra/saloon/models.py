from django.db import models


from shared.models import BaseTextModel

# Create your models here.


class Saloon(BaseTextModel):
    complete_name = models.CharField("Nombre completo", max_length=512)
    icon = models.ImageField("Logo", blank=True, null=True)
    address = models.CharField("Direccion", max_length=512, blank=True, null=True)
    city = models.CharField("Ciudad", max_length=512, blank=True, null=True)
    hours = models.CharField("Horario", max_length=512, blank=True, null=True)
    phone = models.CharField("Telefono", max_length=512, blank=True, null=True)
    web = models.CharField("Web", max_length=512, blank=True, null=True)
    email = models.CharField("E-mail", max_length=512, blank=True, null=True)
    facebook = models.CharField("Facebook", max_length=512, blank=True, null=True)
    reference = models.BooleanField("Referente", default=False)
    maps = models.CharField("Link a google maps", max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = "Camara"
        verbose_name_plural = "Camaras"

    def __str__(self) -> str:
        return self.title


class Link(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=256)
    url = models.CharField(verbose_name="URL", max_length=256)
    image = models.ImageField(
        upload_to="media/", verbose_name="Imagen", blank=True, null=True
    )
    is_available = models.BooleanField(verbose_name="Habilitado", default=False)

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"

    def __str__(self) -> str:
        return self.title


class ImportantAgreement(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=256)
    url = models.CharField(verbose_name="URL", max_length=256)
    image = models.ImageField(
        upload_to="media/", verbose_name="Imagen", blank=False, null=False
    )
    is_available = models.BooleanField(verbose_name="Habilitado", default=False)

    class Meta:
        verbose_name = "Convenio destacado"
        verbose_name_plural = "Convenios destacados"

    def __str__(self) -> str:
        return self.title
