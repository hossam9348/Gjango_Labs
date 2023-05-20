from django import forms
from .models import *


class Update(forms.ModelForm):
    class Meta:
        model=Trainee
        fields='__all__'

class Add(forms.Form):
    name=forms.CharField(required=True)
