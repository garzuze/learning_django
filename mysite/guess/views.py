from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

def check_guess(guess):
        if guess.lower() != 'fabio dos santos reszko junior':
            message = "é nada tu é muito burro"
        else:
            message = "acerto, tu é muito foda"
        
        return message

class Guess(View):
    def get(self, request):
        msg = request.session.get('msg', False)
        if (msg) : del(request.session['msg'])
        return render(request, 'guess/guess.html', {'message': msg})
    
    def post(self, request):
        guess = request.POST.get('guess')
        msg = check_guess(guess)
        request.session['msg'] = msg
        return redirect(request.path)