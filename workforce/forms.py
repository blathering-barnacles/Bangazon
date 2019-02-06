from django import forms
# from django.forms.widgets import SelectDateWidget
from .models import Department



class AddDeptForm(forms.Form):
    department_name = forms.CharField(label='Department Name', max_length=20)
    department_budget = forms.IntegerField(label='Department Budget')