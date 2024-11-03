from CrudCompleto.CrudApp import forms
from .models import ListModel

class ListForm(forms.ListModel):
	class Meta:
		fields = ['titulo']