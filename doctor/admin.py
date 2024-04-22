from django.contrib import admin
from .models import Specialties, MedicalData, OpenDate

# Register your models here.
admin.site.register(Specialties)
admin.site.register(MedicalData)
admin.site.register(OpenDate)