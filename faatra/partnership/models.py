from django.db import models

# Create your models here.


class Partnership(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=256)
    url = models.CharField(verbose_name="Link", max_length=512)
    icon = models.ImageField(verbose_name="Icono", blank=True, null=True)

    class Meta:
        verbose_name = "Convenio"
        verbose_name_plural = "Convenios"

    def __str__(self) -> str:
        return self.name
