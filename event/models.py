from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

Type_event = {
    ('Travel Organize','Travel Organize'),
    ('Event','Event'),
    ('Event of the season','Event of the season'),
    ('Tour Organize','Tour Organize'),
    ('Business event','Business Event'),
    
}




def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return f"events/{instance.id}.{extension}"

class Event(models.Model): # Nom de la table
    Images= models.ImageField(upload_to=image_upload , null=True, blank=True)
    Titre = models.CharField(max_length=100)        # Partie Colonnes
    Pays = models.CharField(max_length=100, null=True, blank=True)
    Nbr_jours = models.CharField(max_length=100, null=True, blank=True)
    Groupe_size = models.IntegerField (default=0, null=True, blank=True)
    Type = models.CharField(max_length=100 , choices=Type_event)
    Localisation = models.CharField(max_length=100)
    Description = RichTextUploadingField()  # Utilisation de CKEditor 5
    Programme = models.TextField(max_length=2000)
    Include  = models.TextField(max_length=1000, default="", null=True, blank=True)
    Public_date =  models.DateTimeField(auto_now=True, null=True, blank=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # Champs pour les prix et la devise
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD')
    event_date = models.DateField(null=True, blank=True)  # Ajoutez ce champ pour la date de l'événement

    slug = models.SlugField(null=True, blank=True)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.Titre)
        super(Event,self).save(*args, **kwargs)
    

    
    
    def __str__(self):
        return self.Titre
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name




