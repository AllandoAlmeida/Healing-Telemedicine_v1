from django.urls import path
from . import views

urlpatterns = [
    path('register_doctor/', views.register_doctor, name="register_doctor"),    
    path('open_calendar/', views.open_calendar, name="open_calendar"),    
    path('queries_doctor/', views.queries_doctor, name="queries_doctor"),    
]