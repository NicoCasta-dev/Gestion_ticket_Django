from django.db import models
import datetime

class Tickets_Ouverts(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
        return self.titre + ' ' + self.description + ' ' + self.date
    
class utilisateurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now)
    numero_employe = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.nom + ' ' + self.prenom + ' ' + self.date + ' ' + self.numero_employe