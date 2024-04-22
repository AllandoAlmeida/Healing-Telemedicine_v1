from django.shortcuts import render, redirect
from .models import Specialties, MedicalData, is_doctor
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.

def register_doctor(request):
    
    if is_doctor(request.user):
        messages.add_message(request, constants.WARNING, 'Você ja está cadastro como médico')
        return redirect('/doctors/schedule_time')
        
    if request.method == "GET":
        specialties = Specialties.objects.all()
        for i in specialties:            
            print(i.id, i.specialty)        
        return render(request, 'register_doctor.html', {'specialties':specialties})
    elif request.method == "POST":
        name = request.POST.get('nome')
        zidCode = request.POST.get('cep')
        street = request.POST.get('rua')
        neighborhood = request.POST.get('bairro')
        number = request.POST.get('numero')
        description = request.POST.get('descricao')
        query_value = request.POST.get('valor_consulta')
        crm = request.POST.get('crm')
        medical_identity_card = request.FILES.get('cim')
        register_geral = request.FILES.get('rg')
        photo = request.FILES.get('foto')
        specialty_id = request.POST.get('especialidade')  # Obtendo o ID da especialidade
        
        medical_data = MedicalData(
            user=request.user,
            name=name,
            zidCode=zidCode,
            street=street,
            neighborhood=neighborhood,
            number=number,
            description=description,
            query_value=query_value,
            crm=crm,
            medical_identity_card=medical_identity_card,
            register_geral=register_geral,
            photo=photo,
            specialty_id=specialty_id  # Atribuindo o ID da especialidade
        )
        print(medical_data)
        medical_data.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso')
        return redirect('/doctors/schedule_time')
