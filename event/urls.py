
from . import views
from django.urls import path , include


urlpatterns = [
    path('',views.event_list),
    path('<int:id>',views.event_detail),
]
