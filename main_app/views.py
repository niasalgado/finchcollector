from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from . models import Finch, Birdhouse
from . forms import FeedingForm

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
    id_list = finch.birdhouses.all().values_list('id') # [1, 3, 7]
    # generate a list of birdhouses while excludes the ones containing ids included in the id_list
    birdhouses_finch_doesnt_have = Birdhouse.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/details.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'birdhouses': birdhouses_finch_doesnt_have
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    # validate the form
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        '''
        {
            meal: 'B',
            date: '2023-06-02',
            cat_id: 1
        }
        '''
        new_feeding.save()
    return redirect('details', finch_id=finch_id)

def assoc_birdhouse(request, finch_id, birdhouse_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Finch.objects.get(id=finch_id).birdhouses.add(birdhouse_id)
  return redirect('details', finch_id=finch_id)

def unassoc_birdhouse(request, finch_id, birdhouse_id):
  Finch.objects.get(id=finch_id).birdhouses.remove(birdhouse_id)
  return redirect('details', finch_id=finch_id)

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

class BirdhouseCreate(CreateView):
    model = Birdhouse
    fields = ['size', 'color']

class BirdhouseList(ListView):
    model = Birdhouse

class BirdhouseDetail(DetailView):
    model = Birdhouse

class BirdhouseUpdate(UpdateView):
    model = Birdhouse
    fields = ['size', 'color']

class BirdhouseDelete(DeleteView):
    model = Birdhouse
    success_url = '/birdhouses/'