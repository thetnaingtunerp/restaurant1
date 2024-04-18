from django import forms
from .models import *


class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class tablenameform(forms.ModelForm):
    class Meta:
        model = tablename
        fields = ['table_name','occupy']
        widgets = {
            'table_name': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'occupy': forms.TextInput(attrs={'class': 'form-control col-md-6'}),

        }

class itemcreateform(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'