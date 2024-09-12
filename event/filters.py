from django import forms
import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
        Titre = django_filters.ChoiceFilter(
        choices=[],  # Cette liste sera remplie dynamiquement
        label='Titre',
        widget=forms.Select(attrs={'class': 'form-control'})
        )
        Pays = django_filters.ChoiceFilter(
            choices=[],  # Cette liste sera remplie dynamiquement
            label='Pays',
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        event_date = django_filters.DateFilter(
            field_name='event_date',
            lookup_expr='exact',
            label='Date',
            widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'})
        )
        price = django_filters.NumberFilter(
            field_name='price',
            lookup_expr='exact',
            label='Price',
            widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
        class Meta:
            model = Event
            fields = ['Titre', 'Pays', 'event_date', 'price']
            
            
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        # Remplir dynamiquement les choix
            self.filters['Titre'].extra['choices'] = [(titre, titre) for titre in Event.objects.values_list('Titre', flat=True).distinct()]
            self.filters['Pays'].extra['choices'] = [(pays, pays) for pays in Event.objects.values_list('Pays', flat=True).distinct()]
        