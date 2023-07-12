from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

class Hello(View):
    def get(self, request):
        # request.session é um dicionário que já vem junto com cada sessão de cada browser
        # esse dicionário tem uma chave chamada 'num_visits' que o valor default é  0
        # toda vez que a nossa view de get for acionada, nós adicionamos 1 a esse valor
        num_visits = request.session.get('num_visits', 0) + 1
        request.session['num_visits'] = num_visits
        if num_visits > 4: del(request.session['num_visits'])
        return render(request, 'hello/hello.html', {'num_visits': str(num_visits)})