from . models import Staff
from django import forms

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields=[
            'name','address','age'
        ]