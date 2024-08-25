from django.db import models

# Create your models here.

Type_event = {
    ('Travel Organize','Travel Organize'),
    ('Event','Event'),
    ('Event of the season','Event of the season'),
    ('Tour Organize','Tour Organize'),
    ('Business event','Business Event'),
    
}



class Event(models.Model): # Nom de la table
    Images= models.ImageField(upload_to='Voy')
    Titre = models.CharField(max_length=100)        # Partie Colonnes
    Pays = models.CharField(max_length=100)
    Nbr_jours = models.CharField(max_length=100)
    Groupe_size = models.IntegerField (default=0)
    Type = models.CharField(max_length=100 , choices=Type_event)
    Localisation = models.CharField(max_length=100)
    Description = models.TextField(max_length=2000, default="")
    Programme = models.TextField(max_length=2000)
    Include  = models.TextField(max_length=1000, default="")
    Public_date =  models.DateTimeField(auto_now=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Titre
    
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
