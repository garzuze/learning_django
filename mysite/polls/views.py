from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def index(request):
    return render(request, 'registration/login.html')

def check_guess(guess):
        if guess != 'giovana':
            message = "é nada tu é muito burro"
            img_link = ""
        else:
            message = "acerto, tu é muito foda"
            img_link = "/static/polls/acerto.jpg"
            # <img src=" {% static '../static/polls/acerto.jpg' %}" alt="o caraio">
        
        return [message, img_link]

class Guess(View):
    def get(self, request):
        return render(request, 'guess.html')
    
    def post(self, request):
        guess = request.POST.get('guess')
        msg = check_guess(guess)
        return render(request, 'guess.html', {'message' : msg[0], 'image': msg[1]})
    