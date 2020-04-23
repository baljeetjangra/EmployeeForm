from django.forms import forms, ModelForm
from .models import Employee


class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ('__all__')
        labels = {

        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False
