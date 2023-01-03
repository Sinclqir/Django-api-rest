from django.db import models

# Create your models here.

class Concessionnaire(models.Model):
    nom = models.CharField(max_length=50)
    numero_siret = models.IntegerField(max_length=15)
    code_postal = models.CharField(max_length=5)

class Voiture(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    chevaux = models.IntegerField()
    concessionnaire = models.ForeignKey(Concessionnaire, on_delete=models.CASCADE)