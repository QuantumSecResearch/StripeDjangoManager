from django.db import models

# Create your models here.
class PageVisit(models.Model):
    #db->table
    #id->primary 
    path = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
