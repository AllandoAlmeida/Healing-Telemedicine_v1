from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('select_times/<int:id_medical_data>', views.select_times, name="select_times"),
    path('schedule_time/<int:open_date_id>', views.schedule_time, name="schedule_time"),
    path('my_queries/', views.my_queries, name="my_queries"),
]