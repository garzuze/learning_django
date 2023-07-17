from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views import generic
from django.urls import reverse_lazy

from autos.models import Auto, Make


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        make_count = Make.objects.all().count() # contador de montadoras
        auto_list = Auto.objects.all() # lista de automoveis
        context = {'make_count': make_count, 'auto_list': auto_list}

        return render(request, 'autos/auto_list.html', context)


class MakeListView(LoginRequiredMixin, generic.ListView):
    model = Make


class MakeCreate(LoginRequiredMixin, generic.CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
    

class MakeDelete(LoginRequiredMixin, generic.DeleteView):
    model = Make
    fiels = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoCreate(LoginRequiredMixin, generic.CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, generic.DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


# Usamos reverse_lazy em vez de reverse nos atributos da classe
# porque views.py é carregado por urls.py e em urls.py as_view() faz com que
# o construtor da classe de visualização seja executado antes que o urls.py tenha sido
# completamente carregado e o urlpatterns tenha sido processado.