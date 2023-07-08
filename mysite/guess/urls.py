from django.urls import path

from . import views

urlpatterns = [
    path('', views.Guess.as_view(), name='guess'),
]