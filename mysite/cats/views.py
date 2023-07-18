from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views import generic
from django.urls import reverse_lazy

from .models import Breed, Cat

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        cat_list = Cat.objects.all()
        breed_count = Breed.objects.all().count()
        context = {'cat_list': cat_list, 'breed_count': breed_count}

        return render(request, 'cats/cat_list.html', context)
    
class BreedList(LoginRequiredMixin, generic.ListView):
    model = Breed

class BreedCreate(LoginRequiredMixin, generic.CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, generic.DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatCreate(LoginRequiredMixin, generic.CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, generic.DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')