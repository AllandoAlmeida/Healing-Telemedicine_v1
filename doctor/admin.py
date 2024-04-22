from django.contrib import admin
from .models import Specialties, MedicalData

# Register your models here.
admin.site.register(Specialties)
admin.site.register(MedicalData)