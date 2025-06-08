from django.forms import ModelForm
from .models import Incription

# Create the form class
class IncriptionForm(ModelForm):
    class Meta:
        model = Incription
        fields = [
            "fullname",
            "email",
            "telefono",
            "dni",
            "birth_date",
            "address",
            "zip_code",
            "city",
            "county",
            "employee_condition",
            "comment"
        ]