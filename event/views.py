from django.shortcuts import render
from .models import Event


# Create your views here.
def event_list(request):
    event_list = Event.objects.all()
    context={'events': event_list}
    return render(request,'event/event_list.html',context)




def event_detail(request , id):
    event_detail = Event.objects.get(id=id)
    context={'event': event_detail}
    return render(request,'event/event_detail.html',context)