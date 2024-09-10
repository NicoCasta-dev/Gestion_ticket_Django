from django.db import models
import datetime
from django.contrib.auth.models import User


class Tickets_Ouverts(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=datetime.datetime.now)
    #auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('ouvert', 'Ouvert'), ('fermé', 'Fermé')], default='ouvert')


    def __str__(self):
        return self.titre + ' ' + self.description + ' ' + self.date + ' ' + self.status
    
class utilisateurs(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now)
    numero_employe = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.nom + ' ' + self.prenom + ' ' + self.date + ' ' + self.numero_employe