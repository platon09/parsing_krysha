from django import forms

from .models import Apartments


class ApartmentsForm(forms.ModelForm):


	class Meta:
		model = Apartments
		fields = (
			'name',
			'price',
			'location',
			'url',
			)
		widgets = {
			'name': forms.TextInput,
			'location': forms.TextInput,
		}