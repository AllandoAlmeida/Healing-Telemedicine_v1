from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from doctor.models import MedicalData, OpenDate, Specialties, is_doctor
from django.contrib.messages import constants
from django.contrib import messages

from django import template
from django.utils.formats import date_format

from patient.models import Query



# Create your views here.
def home(request):
    if request.method == "GET":
        doctors = MedicalData.objects.all()
        specialties = Specialties.objects.all()
        doctor_filter = request.GET.get('medico')
        filter_by_specialties = request.GET.getlist('especialidades')
        
        if doctor_filter:
            doctors = doctors.filter(name__icontains=doctor_filter)
        
        if filter_by_specialties:
            doctors = doctors.filter(specialty_id__in=filter_by_specialties)
        
        if not doctors.exists():  
            messages.add_message(request, constants.WARNING, 'Lamentamos! não foi possível localizar o médico pesquisado.')
            return redirect('/patient/home/')        
        
        return render(request, 'home.html', {'doctors': doctors, 'specialties': specialties, 'is_doctor': is_doctor(request.user)})
    

register = template.Library()
    
@register.filter
def month_in_words(value):
    month = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    return month[value - 1]

@register.filter
def day_week_in_extension(value):
    days_week = ("Segunda-feira", "Terça-feira", "Quarta-feira",
                "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")
    return days_week[value]

   
def select_times(request, id_medical_data):
   
    
    if request.method == "GET":
        doctor = MedicalData.objects.get(id=id_medical_data)
        available_dates = OpenDate.objects.filter(user=doctor.user).filter(date__gt=datetime.now()).filter(scheduled=False).order_by('date')
        return render(request, 'select_times.html', {'doctor': doctor, 'available_dates': available_dates, 'is_doctor': is_doctor(request.user)})
 
   
def schedule_time(request, open_date_id):
    if request.method == "GET":
        open_date = OpenDate.objects.get(id=open_date_id)

        scheduled_time = Query(
            patient=request.user,
            open_date=open_date
        )

        scheduled_time.save()

        # TODO: Sugestão Tornar atomico

        open_date.scheduled = True
        open_date.save()

        messages.add_message(request, constants.SUCCESS, 'Horário agendado com sucesso.')

        return redirect('/patient/my_queries/')
    
def my_queries(request):
    # realizar os filtros
    if request.method == "GET":
            queries_scheduled = Query.objects.filter(patient=request.user).filter(open_date__date__gte=datetime.now())
            print("my_querys", queries_scheduled)
            return render(request, 'my_queries.html', {'queries_scheduled': queries_scheduled, 'is_doctor': is_doctor(request.user)})
        
        
def query(request, id_query):
    if request.method == 'GET':
        query = Query.objects.get(id=id_query)
        medical_data = MedicalData.objects.get(user=query.open_date.user)
        return render(request, 'query.html', {'query': query, 'medical_data': medical_data, 'is_doctor': is_doctor(request.user)})

         