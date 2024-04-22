from django.db import models
from django.contrib.auth.models import User

def is_doctor(user):
    return MedicalData.objects.filter(user=user).exists()

# Create your models here.
class Specialties(models.Model):    
    specialty = models.CharField(max_length=100)
    

    def __str__(self):
         return self.specialty


class MedicalData(models.Model):
     crm = models.CharField(max_length=30)
     name = models.CharField(max_length=100)
     zidCode = models.CharField(max_length=15)
     street = models.CharField(max_length=100)
     neighborhood = models.CharField(max_length=100)
     number = models.IntegerField()
     register_geral = models.ImageField(upload_to="rgs")
     medical_identity_card = models.ImageField(upload_to='mic')
     photo = models.ImageField(upload_to="fotos_profil")
     description = models.TextField(null=True, blank=True)
     query_value = models.FloatField(default=100)
     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
     specialty = models.ForeignKey(Specialties, on_delete=models.DO_NOTHING, null=True, blank=True)

     def __str__(self):
         return self.user.username
     

""" 
     class Especialidades(models.Model):
        especialidade = models.CharField(max_length=100)
        icone = models.ImageField(upload_to="icones", null=True, blank=True)

        def __str__(self):
            return self.especialidade


    class DadosMedico(models.Model):
        crm = models.CharField(max_length=30)
        nome = models.CharField(max_length=100)
        cep = models.CharField(max_length=15)
        rua = models.CharField(max_length=100)
        bairro = models.CharField(max_length=100)
        numero = models.IntegerField()
        rg = models.ImageField(upload_to="rgs")
        cedula_identidade_medica = models.ImageField(upload_to='cim')
        foto = models.ImageField(upload_to="fotos_perfil")
        user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
        descricao = models.TextField(null=True, blank=True)
        especialidade = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING, null=True, blank=True)
        valor_consulta = models.FloatField(default=100)

        def __str__(self):
            return self.user.username
     
     """