from django.shortcuts import redirect, render , get_object_or_404
from .models import Event
from django.core.paginator import Paginator
from .filters import EventFilter
from .forms import ApplyForm

def event_list(request):
    # Définir l'ordre de tri par défaut comme décroissant par date de publication
    sort_order = request.GET.get('sort', '-Public_date')
    
    # Liste des événements triés selon l'ordre choisi
    
    event_list = Event.objects.all().order_by(sort_order)
    available_dates = list(Event.objects.values_list('event_date', flat=True).distinct())
    
    # Filters:
    myfilter=EventFilter(request.GET,queryset=event_list)
    event_list=myfilter.qs
    # Get unique locations for the filter
    
    
    
    
    # Calculer le nombre total d'événements
    total_events = event_list.count()
    
    #page generateur 
    paginate_by = request.GET.get("paginate_by", 9)
    
    
    paginator = Paginator(event_list, int(paginate_by))
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    # Filters:
    
    myfilter=EventFilter(request.GET,queryset=event_list)
    
    context={
        'events': page_obj,
        'myfilter':myfilter,
        'paginate_by': paginate_by,
        'total_events': total_events,
        'sort_order': sort_order, 
        'available_date' : available_dates,
        }
    
    return render(request,'event/event_list.html',context)




def event_detail(request , slug):
    event_detail = Event.objects.get(slug=slug)
    context={'event': event_detail}
    return render(request,'event/event_detail.html',context)


def booking(request, slug):
    event = Event.objects.get(slug=slug)  # Récupère l'événement par slug
    if request.method == 'POST':
        form = ApplyForm(request.POST, event=event)  # Passe l'événement au formulaire
        if form.is_valid():
            apply_instance = form.save(commit=False)
            apply_instance.event = event  # Associe l'événement à l'instance Apply
            number_of_people = form.cleaned_data['number_of_people']
            if number_of_people >= 0:
                apply_instance.price = event.price * number_of_people  # Calcule le prix total
                apply_instance.save()
                return redirect('booking_success')
            else:
                form.add_error('number_of_people', 'Le nombre de personnes ne peut pas être négatif.')

    else:
        form = ApplyForm(event=event)  # Initialise le formulaire avec l'événement

    context = {'form': form, 'event': event}  # Passe l'événement au contexte
    return render(request, 'event/booking.html', context)

    
    