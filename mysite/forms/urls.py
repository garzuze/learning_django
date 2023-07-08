from django.urls import path

from . import views

urlpatterns = [
    path('', views.Form.as_view(), name='forms'),
]