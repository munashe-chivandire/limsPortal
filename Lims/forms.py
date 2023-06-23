from django import forms
from .models import *
from django.forms import DateInput


class conpi_forms(forms.ModelForm):
    class Meta:
        model = conpi
        fields = "__all__"
        exclude = ('date_created', 'date_updated','status','interest')
        widgets = {
            'farm_name': forms.TextInput(attrs={'class':'form-control'}),
            'district': forms.Select(attrs={'class':'form-control'}),
            'title_deed_number': forms.TextInput(attrs={'class':'form-control'}),
            'farm_category': forms.TextInput(attrs={'class':'form-control'}),
            'farm_owner_name': forms.TextInput(attrs={'class':'form-control'}),
            'name_of_applicant': forms.TextInput(attrs={'class':'form-control'}),
            'contact_details': forms.TextInput(attrs={'class':'form-control'}),
            'reason_for_applying': forms.Select(attrs={'class':'form-control'}),
            'number_of_settlers': forms.NumberInput(attrs={'class':'form-control'}),
            'reasons_for_conpi': forms.TextInput(attrs={'class':'form-control'}),
            'signatue': forms.FileInput(attrs={'class':'form-control'}),
            'other': forms.FileInput(attrs={'class':'form-control'}),
        

    }