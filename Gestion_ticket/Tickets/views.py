from django.shortcuts import render,redirect
from . import models
from .forms import *

def tickets_ouverts(request):
    tickets = models.Tickets_Ouverts.objects.all()
    return render(request, 'tickets_ouverts.html', {'tickets': tickets})

def ajouter_ticket(request):
    if request.method == 'POST':
        form = TicketsOuvertsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets_ouverts')
    else:
        form = TicketsOuvertsForm()
    
    return render(request, 'ajouter_ticket.html', {'form': form})