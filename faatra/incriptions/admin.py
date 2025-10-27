from django.contrib import admin

# Register your models here.

from django.contrib import admin

from import_export.admin import ExportActionModelAdmin
from import_export import fields
from import_export.resources import ModelResource
from .models import Incription, EmployeeCondition
from django.db.models import Q
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

    def get_queryset(self):
        """
        Optimize queries by prefetching related objects to avoid N+1 queries
        """
        return super().get_queryset().select_related('employee_condition', 'course', 'course__saloon')

    class Meta:
        model = Incription
        fields = ("fullname", "email", "telefono", "dni", "birth_date", "address", "zip_code", "city", "county", "comment", "is_confirmed", "created_date", "employee_condition__name", "course__title")

class SaloonTitleFilter(admin.SimpleListFilter):
    title = "Cámara"  # Nombre del filtro en el admin
    parameter_name = "saloon_title"  # Nombre del parámetro en la URL

    def lookups(self, request, model_admin):
        """Devuelve las opciones del filtro (cámaras disponibles)"""
        saloons = set(model_admin.model.objects.values_list("course__saloon__title", flat=True))
        return [(s, s) for s in saloons if s]  # Filtra los valores no vacíos

    def queryset(self, request, queryset):
        """Aplica el filtro cuando se selecciona un valor"""
        if self.value():
            return queryset.filter(Q(course__saloon__title=self.value()))
        return queryset 

@admin.register(Incription)
class IncriptionAdmin(ExportActionModelAdmin):
    resource_class = InscriptionResource
    list_display = ("fullname", "email", "created_date", "course", "is_confirmed", "get_saloon")
    list_editable = ("is_confirmed",)

    def get_queryset(self, request):
        """
        Optimize list view queries with select_related
        """
        qs = super().get_queryset(request)
        return qs.select_related('employee_condition', 'course', 'course__saloon')

    def get_saloon(self, obj):
        return obj.course.saloon.title if obj.course and obj.course.saloon else "-"
    get_saloon.short_description = "Cámara"

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
    list_filter = ("is_confirmed", "created_date", "course", SaloonTitleFilter, )

