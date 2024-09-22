
from . import views
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.event_list , name='event_list'),
    path('<str:slug>/', views.event_detail,name='event_detail'),
    path('<str:slug>/booking/', views.booking, name='booking'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)