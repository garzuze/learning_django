from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def hello(request):
    # request.session é um dicionário que já vem junto com cada sessão de cada browser
    # esse dicionário tem uma chave chamada 'num_visits' que o valor default é  0
    # toda vez que a nossa view de get for acionada, nós adicionamos 1 a esse valor
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del(request.session['num_visits'])

    oldval = request.COOKIES.get('zap', None) # Pega um cookie ainda inexistente

    # html que será exibido na página
    resp = HttpResponse(f"O cookie zapzap eh {str(oldval)}"
                        f"<br>o cookie sakai car eh: {request.COOKIES.get('sakaicar')}"
                         f"<br>view count={num_visits}")
    
    if oldval: 
        resp.set_cookie('zap', int(oldval)+1) # Adiciona um ao cookie que antes não tinha nada
        # esse cookie vai existir até o browser fechar porque não tem data para expirar
    else : 
        resp.set_cookie('zap', 42)
    resp.set_cookie('sakaicar', 42, max_age=1000) # max_age = segundos para expirar
    resp.set_cookie('dj4e_cookie', '3d5caa90', max_age=1000) # mais um cookie

    return resp