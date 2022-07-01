from django.db import models
from shared.models import BaseTextModel

# Create your models here.
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    location = models.TextField(verbose_name="Dirección", max_length=1024)
    phone = models.TextField(verbose_name="Número de contacto", max_length=1024)
    email = models.TextField(verbose_name="Email de contacto", max_length=1024)
    attention = models.TextField(verbose_name="Horario de atencion", max_length=1024)

    def __str__(self):
        return "Faatra configuraciónes"

    class Meta:
        verbose_name = "Faatra configuraciónes"


class SocialMediaConfiguration(SingletonModel):
    wsp = models.TextField(verbose_name="Link a Whatsapp", max_length=1024)
    youtube = models.TextField(verbose_name="Link a Youtube", max_length=1024)
    twitter = models.TextField(verbose_name="Link a twitter", max_length=1024)
    instagram = models.TextField(verbose_name="Link a instagram", max_length=1024)
    facebook = models.TextField(verbose_name="Link a facebook", max_length=1024)
    linkedin = models.TextField(verbose_name="Link a linkedin", max_length=1024)
    snit_description = models.TextField(verbose_name="Descripcion de SNIT", max_length=1024)
    snit_url = models.TextField(verbose_name="Link a SNIT", max_length=1024)

    def __str__(self):
        return "Faatra redes sociales configuraciónes"

    class Meta:
        verbose_name = "Faatra redes sociales configuraciónes"


class WhoWeAre(SingletonModel, BaseTextModel):

    class Meta:
        verbose_name = "Quienes somos"
        verbose_name_plural = "Quienes somos"

    def __str__(self) -> str:
        return self.title
