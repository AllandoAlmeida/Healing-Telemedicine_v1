from django.urls import path
from . import views

urlpatterns = [
    path('register_doctor/', views.register_doctor, name="register_doctor"),    
    path('open_calendar/', views.open_calendar, name="open_calendar"),    
    path('queries_doctor/', views.queries_doctor, name="queries_doctor"), 
    path('consultation_area_doctor/<int:id_query>', views.consultation_area_doctor, name="consultation_area_doctor"), 
    path('add_documento/<int:id_consulta>/', views.add_documento, name="add_consulta"),
]