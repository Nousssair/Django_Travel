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
            'nationality', 
            'number_of_people', 
            'event',  # Assurez-vous que ce champ existe dans le modèle Apply
        ]
        widgets = {
            'event': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event', None)
        super().__init__(*args, **kwargs)
        
        if event:
            self.fields['event'] = forms.ModelChoiceField(queryset=Event.objects.filter(pk=event.pk), widget=forms.HiddenInput())
            # Remplacer les champs par des lectures des attributs de l'événement
            self.fields['title'] = forms.CharField(initial=event.Titre, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['country'] = forms.CharField(initial=event.Pays, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['location'] = forms.CharField(initial=event.Localisation, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['price'] = forms.DecimalField(initial=event.price, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['currency'] = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR')], initial=event.currency, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['event_date'] = forms.DateField(initial=event.event_date, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            
    def clean(self):
        cleaned_data = super().clean()
        
        # Exemple de validation conditionnelle
        if not cleaned_data.get('event'):
            self.add_error('event', 'Cet événement est requis.')
        
        return cleaned_data        
