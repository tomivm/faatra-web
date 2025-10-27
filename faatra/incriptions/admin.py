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
    course_title = fields.Field(attribute='course__title', column_name='Curso')
    course_saloon = fields.Field(attribute='course__saloon__title', column_name='Cámara')
    employee_condition_name = fields.Field(attribute='employee_condition__name', column_name='Condición Laboral')
    course_category = fields.Field(attribute='course__category__title', column_name='Categoría')
    course_topic = fields.Field(attribute='course__topic__title', column_name='Tema')
    course_mode = fields.Field(attribute='course__mode__description', column_name='Modalidad')
    course_duration = fields.Field(attribute='course__duration', column_name='Duración')
    course_city = fields.Field(attribute='course__city', column_name='Ciudad del Curso')
    course_instructor = fields.Field(attribute='course__in_charge', column_name='Instructor')

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
        Ultra-optimized queryset with all related objects loaded in one query
        """
        return super().get_queryset().select_related(
            'employee_condition',
            'course',
            'course__saloon',
            'course__category',
            'course__topic',
            'course__mode'
        ).order_by('-created_date')

    def filter_export(self, queryset, **kwargs):
        """
        Optional filtering to reduce export size - can be customized based on needs
        """
        # Example: Only export confirmed inscriptions
        # return queryset.filter(is_confirmed=True)
        return queryset

    def get_export_data(self, file_format, queryset=None, **kwargs):
        """
        Override to handle large datasets efficiently
        """
        if queryset is None:
            queryset = self.get_queryset()

        # Use iterator for large datasets to avoid loading all objects into memory
        if queryset.count() > 1000:
            return super().get_export_data(file_format, queryset.iterator(chunk_size=1000), **kwargs)

        return super().get_export_data(file_format, queryset, **kwargs)

    def dehydrate_fullname(self, inscription):
        """Ensure fullname is properly formatted"""
        return inscription.fullname.strip() if inscription.fullname else ""

    def dehydrate_email(self, inscription):
        """Ensure email is lowercase and stripped"""
        return inscription.email.lower().strip() if inscription.email else ""

    def dehydrate_created_date(self, inscription):
        """Format date consistently"""
        return inscription.created_date.strftime('%d/%m/%Y %H:%M') if inscription.created_date else ""

    class Meta:
        model = Incription
        fields = (
            "fullname", "email", "telefono", "dni", "birth_date", "address",
            "zip_code", "city", "county", "comment", "is_confirmed", "created_date",
            "employee_condition_name", "course_title", "course_saloon",
            "course_category", "course_topic", "course_mode", "course_duration",
            "course_city", "course_instructor"
        )
        export_order = (
            "created_date", "fullname", "email", "telefono", "dni", "birth_date",
            "address", "zip_code", "city", "county", "course_title", "course_saloon",
            "course_category", "course_topic", "course_mode", "course_duration",
            "course_city", "course_instructor", "employee_condition_name",
            "comment", "is_confirmed"
        )

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

