from django import forms
from .models import UberInformation

class UberInformationForm(forms.ModelForm):
    class Meta:
        model = UberInformation
        
        fields = [
			'name',
            'street',
            'postalcode',
            'city',
		]
        
        labels = {
			'name': 'Name',
            'street':'Street',
            'postalcode':'Postal Code',
            'city':'City',
		}