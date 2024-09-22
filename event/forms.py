from django import forms
from .models import Apply, Event  # Assurez-vous d'importer le modèle Event
from django_countries.fields import CountryField


class ApplyForm(forms.ModelForm):
    
    nationality = CountryField().formfield()
    number_of_people = forms.IntegerField(initial=0, min_value=0)

    class Meta:
        model = Apply
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phone_number', 
            'nationality', 
            'number_of_people', 
        ]
        

    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event', None)
        super().__init__(*args, **kwargs)
        
        if event:
            self.fields['event'] = forms.ModelChoiceField(queryset=Event.objects.filter(pk=event.pk), widget=forms.HiddenInput())
            self.fields['title'] = forms.CharField(initial=event.Titre, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['country'] = forms.CharField(initial=event.Pays, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['location'] = forms.CharField(initial=event.Localisation, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['price'] = forms.DecimalField(initial=event.price, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['currency'] = forms.ChoiceField(initial=event.currency, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['event_date'] = forms.DateField(initial=event.event_date, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
