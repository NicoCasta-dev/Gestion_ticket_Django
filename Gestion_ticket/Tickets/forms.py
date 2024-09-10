from django import forms
from django.forms import ModelForm
from .models import Tickets_Ouverts, utilisateurs

class TicketsOuvertsForm(ModelForm):
    class Meta:
        model = Tickets_Ouverts
        fields = '__all__'

class UtilisateursForm(ModelForm):
    class Meta:
        model = utilisateurs
        fields = ['nom', 'prenom', 'numero_employe']

class AjouterTicketForm(ModelForm):
    class Meta:
        model = Tickets_Ouverts
        fields = '__all__'