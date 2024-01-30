from django.contrib import admin
from .models import Patient, MedicalHistory, MedicalStaff, Department, Speciality, Procedure, Appointment, Prescription, ProcedureApplication

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalHistory)
admin.site.register(MedicalStaff)
admin.site.register(Department)
admin.site.register(Speciality)
admin.site.register(Procedure)
admin.site.register(ProcedureApplication)
admin.site.register(Appointment)
admin.site.register(Prescription)