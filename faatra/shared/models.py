import datetime
from django.db import models
from django_quill.fields import QuillField
from django.utils.text import slugify

# Create your models here.


class BaseTextModel(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=256)
    description = models.CharField(verbose_name="resumen", max_length=256)
    content = QuillField()
    image = models.ImageField(
        upload_to="media/", verbose_name="Imagen", blank=True, null=True
    )
    created_date = models.DateTimeField(
        verbose_name="Fecha de creación",
        auto_created=True,
        default=datetime.datetime.now,
    )
    last_modification_date = models.DateTimeField(
        verbose_name="Fecha de la ultima modificación", auto_now_add=True
    )
    is_available = models.BooleanField(verbose_name="Habilitado", default=False)
    url = models.SlugField(max_length=256, unique=True)

    class Meta:
        abstract = True
        verbose_name = "BaseTextModel"
        verbose_name_plural = "BaseTextModel"

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super().save()
