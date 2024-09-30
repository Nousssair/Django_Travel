from django import forms
from .models import Apply, Event  # Assurez-vous d'importer le modèle Event
from django_countries.fields import CountryField

class ApplyForm(forms.ModelForm):
    nationality = CountryField().formfield()
    number_of_people = forms.IntegerField(initial=1, min_value=1)

    class Meta:
        model = Apply
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phone_number',
            'id_passport', 
            'nationality',
            'number_of_people', 
            
        ]
