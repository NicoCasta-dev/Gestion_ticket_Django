from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.tickets_ouverts, name='tickets_ouverts'),
    path('ajouter/', views.ajouter_ticket, name='ajouter_ticket'),
]