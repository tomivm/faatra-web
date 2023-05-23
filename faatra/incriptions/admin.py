from django.contrib import admin

# Register your models here.

from django.contrib import admin

from import_export.admin import ExportActionModelAdmin
from import_export import fields
from import_export.resources import ModelResource
from .models import Incription, EmployeeCondition

# Register your models here.


@admin.register(EmployeeCondition)
class EmployeeConditionAdmin(admin.ModelAdmin):
    pass

class InscriptionResource(ModelResource):
    @classmethod
    def field_from_django_field(self, field_name, django_field, readonly):
        """
        Returns a Resource Field instance for the given Django model field.
        """
        FieldWidget = self.widget_from_django_field(django_field)
        widget_kwargs = self.widget_kwargs_for_field(field_name)
        field = fields.Field(attribute=field_name, column_name=django_field.verbose_name,
                widget=FieldWidget(**widget_kwargs), readonly=readonly)
        return field

    class Meta:
        model = Incription
        fields = ("fullname", "email", "telefono", "dni", "birth_date", "address", "zip_code", "city", "county", "comment", "is_confirmed", "created_date", "employee_condition__name", "course__title")

#@admin.register(Incription)
class IncriptionAdmin(ExportActionModelAdmin):
    resource_class = InscriptionResource
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

admin.site.register(Incription, IncriptionAdmin)