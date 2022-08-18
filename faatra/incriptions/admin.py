from django.contrib import admin

# Register your models here.

from django.contrib import admin

from import_export.admin import ExportActionMixin
from .models import Incription, EmployeeCondition

# Register your models here.


@admin.register(EmployeeCondition)
class EmployeeConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(Incription)
class IncriptionAdmin(ExportActionMixin, admin.ModelAdmin):
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
