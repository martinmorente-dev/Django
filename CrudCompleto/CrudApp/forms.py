from django import forms
from .models import ListModel

class ListForm(forms.ModelForm):
	class Meta:
		model = ListModel
		fields = ['titulo']