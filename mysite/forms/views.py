from django.shortcuts import redirect, render
from django.views import View

from forms.forms import BasicForm

# Create your views here.

class Form(View):
    def get(self, request):
        form = BasicForm()
        context = {'form': form}
        return render(request, 'forms/form.html', context)
    
    def post(self, request):
        return redirect(request.path)