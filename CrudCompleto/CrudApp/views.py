from django.shortcuts import get_object_or_404, render, redirect
from .forms import ListForm
from .models import ListModel

def list_index(request):
	lists = ListModel.objects.all()
	if request.method == 'POST':
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ListForm()
	return render(request, 'list_view.html',{'form':form, 'lists':lists})

def update(request, l_id):
	list_id = get_object_or_404(ListModel, id=l_id)
	if request.method == 'POST':
		form = ListForm(request.POST, instance=list_id)
		if form.is_valid():
			form.save()
			return redirect('list.view')
	else:
		form = ListForm(instance=list_id)
	return render(request, 'list_update_view.html',{'form':form})

def delete(request, l_id):
	list_id = get_object_or_404(ListModel, id=l_id)
	if request.method == 'POST':
		list_id.delete()

	return redirect('list.view')
