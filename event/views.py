from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator
from .filters import EventFilter

# Create your views here.
def tour_grid_view(request):
    
    return render(request, 'tour-grid.html')

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