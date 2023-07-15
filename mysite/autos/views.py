from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
from autos.forms import MakeForm

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        make_count = Make.objects.all().count() # contador de montadoras
        auto_list = Auto.objects.all() # lista de automoveis
        context = {'make_count': make_count, 'auto_list': auto_list}

        return render(request, 'autos/auto_list.html', context)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        make_list = Make.objects.all() # lista de montadoras
        context = {'make_list': make_list}

        return render(request, 'autos/make_list.html', context)


# Usamos reverse_lazy() porque estamos em um código de "atributo de construtor"
# que é executado antes que o urls.py seja completamente carregado

class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        """Só carrega o formulário para ser preenchido"""
        form = MakeForm()
        context = {'form': form}

        return render(request, self.template, context)
    
    def post(self, request):
        """Postar o formulário efetivamente"""
        form = MakeForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)
        
        make = form.save()
        return redirect(self.success_url)

# O MakeUpdate tem código para implementar o fluxo get/post/validate/store
# O AutoUpdate (abaixo) está fazendo a mesma coisa sem código
# e nenhum formulário, estendendo o UpdateView

class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_form.html'

    def get(self, request, pk):
        """Carregar o formulário que será alterado"""
        make = get_object_or_404(self.model, pk=pk) # Pega o modelo que se quer alterar a partir da pk
        form = MakeForm(instance=make) # Recarrega o formumlário para aquela instancia da classe modelo
        context = {'form': form}

        return render(request, self.template, context)
    
    def post(self, request, pk):
        """Posta o formulário efetivamente"""
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)
        
        form.save()
        return redirect(self.success_url)
    

class MakeDelete(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_confirm_delete.html'

    def get(self, request, pk):
        """Exibe uma página confirmando se o usuário quer mesmo deletar"""
        make = get_object_or_404(self.model, pk=pk) # Pega o modelo que se quer alterar a partir da pk
        context = {'make': make}

        return render(request, self.template, context)
    
    def post(self, request, pk):
        """Deletar a make em si"""
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url) # SEMPRE redirecionar o usuário depois do POST
    
# Faça o caminho mais fácil na tabela principal
# Essas exibições não precisam de um formulário porque tem CreateView, etc.
# Crie um objeto de formulário dinamicamente com base nos campos
#  dos atributos do construtor

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# Usamos reverse_lazy em vez de reverse nos atributos da classe
# porque views.py é carregado por urls.py e em urls.py as_view() faz com que
# o construtor da classe de visualização seja executado antes que o urls.py tenha sido
# completamente carregado e o urlpatterns tenha sido processado.