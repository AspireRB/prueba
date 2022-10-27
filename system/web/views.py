from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Data
from .forms import DataForm
# Create your views here.

def start(request):
	return render(request, 'first/start.html')

def data(request):
	data = Data.objects.all()
	return render(request, 'second/index.html', {'data': data})

def create(request):
	form = DataForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('data')
	return render(request, 'second/create.html', {'form': form})

def edit(request, id):
	dato = Data.objects.get(id=id)
	form = DataForm(request.POST or None, instance=dato)
	if form.is_valid() and request.POST:
		form.save()
		return redirect('data')
	return render(request, 'second/edit.html', {'form': form})

def delete(request, id):
	dato = Data.objects.get(id=id)
	dato.delete()
	return redirect('data')