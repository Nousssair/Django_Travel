from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator

# Create your views here.
def tour_grid_view(request):
    
    return render(request, 'tour-grid.html')

def event_list(request):
    event_list = Event.objects.all().order_by('-Public_date')
    
    #page generateur 
    paginator = Paginator(event_list, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context={'events': page_obj}
    
    return render(request,'event/event_list.html',context)




def event_detail(request , slug):
    event_detail = Event.objects.get(slug=slug)
    context={'event': event_detail}
    return render(request,'event/event_detail.html',context)