from django.contrib import admin

# Register your models here.

from django.contrib import admin

from import_export.admin import ExportActionMixin
from import_export.resources import ModelResource
from .models import Incription, EmployeeCondition

# Register your models here.


@admin.register(EmployeeCondition)
class EmployeeConditionAdmin(admin.ModelAdmin):
    pass

class InscriptionResource(ModelResource):
    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            h = h.lower()
            if h == 'created date':
                headers[i] = "Fecha de creacion"
            if h == 'city':
                headers[i] = "Ciudad"
            if h == 'county':
                headers[i] = "Provincia"
            if h == 'birth_date':
                headers[i] = "Fecha de nacimiento"
            if h == 'address':
                headers[i] = "Direccion"
            if h == 'fullname':
                headers[i] = "Nombre completo"
            if h == 'zip_code':
                headers[i] = "Codigo postal"
            if h == 'employee_condition':
                headers[i] = "Nombre completo"
            if h == 'course':
                headers[i] = "Curso"
            if h == 'is_confirmed':
                headers[i] = "Confirmado"
            if h == 'comment':
                headers[i] = "Comentario"
            if h == 'employee_condition':
                headers[i] = "Condicion laboral"
        return headers

    class Meta:
        model = Incription

@admin.register(Incription)
class IncriptionAdmin(ExportActionMixin, admin.ModelAdmin):

    resource_classes = [InscriptionResource]
    list_display = ("fullname", "email", "created_date", "course", "is_confirmed")
    list_editable = ("is_confirmed",)
    fields = (
        "fullname",
        "email",
        "telefono",
        "dni",
        "birth_date",
        "address",
        "zip_code",
        "city",
        "county",
        "course",
        "employee_condition",
        "comment",
        "is_confirmed",
        "created_date",
    )

    readonly_fields = ["created_date"]
    search_fields = ("fullname", "email", "dni")
    list_filter = ("is_confirmed", "created_date", "course")
