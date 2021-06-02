from django import forms
from .models import Information

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        
        fields = [
			'name',
			'gender',
			'age',
            'location',
            'street',
            'postalcode',
		]
        
        labels = {
			'name': 'Name',
			'gender':'Gender',
			'age':'Age',
            'location':'Location',
            'street':'Street',
            'postalcode':'Postal Code',
		}