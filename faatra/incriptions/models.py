from django.db import models
import datetime
from training.models import InformativeOffer
from faatra.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template import Context, Template




class EmployeeCondition(models.Model):
    name = models.CharField("Nombre", max_length=512)

    class Meta:
        verbose_name = "Cond. Laboral"
        verbose_name_plural = "Cond. Laborales"

    def __str__(self) -> str:
        return self.name


class Incription(models.Model):
    fullname = models.CharField("Nombre y apellido", max_length=512)
    email = models.EmailField("email", max_length=512)
    telefono = models.CharField("Telefono", max_length=512)
    dni = models.CharField("DNI", max_length=512)
    birth_date = models.CharField("Fecha de nacimiento", max_length=512)
    address = models.CharField("Direccion", max_length=512)
    zip_code = models.CharField("CP", max_length=512)
    city = models.CharField("Ciudad", max_length=512)
    county = models.CharField("Provincia", max_length=512)
    course = models.ForeignKey(
        InformativeOffer, verbose_name="Curso", max_length=512, on_delete=models.CASCADE
    )
    employee_condition = models.ForeignKey(
        EmployeeCondition,
        verbose_name="Condicion laboral",
        max_length=512,
        on_delete=models.CASCADE,
    )
    comment = models.TextField("Comentarios", blank=True, null=True)
    is_confirmed = models.BooleanField("Confirmado", default=False)

    created_date = models.DateTimeField(
        verbose_name="Fecha de creación",
        auto_created=True,
        default=datetime.datetime.now,
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._is_confirmed = self.is_confirmed

    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"

    def __str__(self) -> str:
        return self.fullname

    def save(self) -> None:
        # if not self._is_confirmed and self.is_confirmed:

        if not self.pk:
            body = f"""Se inscribio {self.fullname}, al curso {self.course.title}.
            Sus datos son:
            Mail: {self.email}
            Telefono: {self.telefono}
            Dirección: {self.address}
            Dni: {self.dni}
            Fecha de nacimiento: {self.birth_date}
            Codido postal: {self.zip_code}
            Comentario: {self.comment}
            """
            send_mail(
                "Incripciones",
                body,
                EMAIL_HOST_USER,
                [self.course.saloon.email],
                fail_silently=False,
            )

            html_template = Template(self.course.email_info.html)

            # Create your context (variables that will be replaced in the template)
            context = Context({'fullname': self.fullname})

            # Render the template with the context
            rendered_html = html_template.render(context)

            body = f"Hola {self.fullname}!"


            send_mail(
                "Incripciones",
                body,
                EMAIL_HOST_USER,
                [self.email],
                fail_silently=False,
                html_message=rendered_html
            )

        super().save()
