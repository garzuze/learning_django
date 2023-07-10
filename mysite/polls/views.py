from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


from .models import Question, Choice
# Usando generic views!!!

# GenericView de lista
class IndexView(generic.ListView): 
    template_name = "polls/index.html" #substitui o nome default que seria polls/question_list
    # como é pra ser exibida uma lista, a gente tem que retornar a lista de objetos
    context_object_name = "latest_question_list"
    # aqui que nós definimos o context_object_name com o get_queryset
    def get_queryset(self):
        """Retorna todas as perguntas publicadas."""
        return Question.objects.order_by("-pub_date")


# GenericView de detalhe
class DetailView(generic.DetailView):
    # É preciso dar o nome do objeto qual a lista de detalhe será mostrada
    model = Question 
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# quando o usuário envia o formulário com sua opção de voto, esse método é a action acionada
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Ele vai pegar qual foi a opção escolhida pelo usuário atráves do valor
        # da opção choice dentro do POST request
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    # Exceções: a escolha do usuário não exite (ele não escolheu)
    except (KeyError, Choice.DoesNotExist):
        # Volta para a tela de detalhe, com uma mensagem de erro
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Você não escolheu nenhuma alternativa.",
            },
        )
    else:
        selected_choice.votes += 1 # Adiciona o voto para a opção escolhida
        selected_choice.save()
        # Sempre retornar um redirect quando estiver trabalhando com post request
        # isso previne que o usuário envie dados duas vezes se apertar o botão de refresh
        # ele vai voltar para a página que o usuário estava anteriormente (args=(question.id))
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))