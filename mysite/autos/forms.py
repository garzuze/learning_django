from django.forms import ModelForm
from autos.models import Make


# Criar a classe de formulário que cria as montadoras
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'