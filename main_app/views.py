from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from . models import Finch

# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finch_details(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/details.html', {'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'species', 'color', 'age']
    # success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'color', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'