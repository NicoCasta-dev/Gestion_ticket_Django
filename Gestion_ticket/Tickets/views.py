from django.shortcuts import render,redirect
from . import models
from .forms import *

def tickets_ouverts(request):
    tickets = models.Tickets_Ouverts.objects.filter(status='ouvert')
    return render(request, 'tickets_ouverts.html', {'tickets': tickets})

def ajouter_ticket(request):
    if request.method == 'POST':
        form = TicketsOuvertsForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 'ouvert'
            ticket.save()
            return redirect('tickets_ouverts')
    else:
        form = TicketsOuvertsForm()
    
    return render(request, 'ajouter_ticket.html', {'form': form})