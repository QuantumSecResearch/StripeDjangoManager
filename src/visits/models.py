from django.db import models

# Create your models here.
class PageVisit(models.Model):
    path = models.CharField(max_length=255, null=False, blank=False) 
    timestamp = models.DateTimeField(auto_now_add=True)  # Champ automatiquement ajouté lors de la création d'un enregistrement
 