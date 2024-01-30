from django import forms
from .models import Patient, MedicalHistory, MedicalStaff, Department, Speciality, Procedure, Appointment, ProcedureApplication, Prescription

class SignInForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField()

class SearchForm(forms.Form):
  search  = forms.CharField(required=False)

class PatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = '__all__'

class MedicalHistoryForm(forms.ModelForm):
  class Meta:
    model = MedicalHistory
    fields = '__all__'

class MedicalStaffForm(forms.ModelForm):
  class Meta:
    model = MedicalStaff
    fields = '__all__'

class DepartmentForm(forms.ModelForm):
  class Meta:
    model = Department
    fields = '__all__'

class SpecialityForm(forms.ModelForm):
  class Meta:
    model = Speciality
    fields = '__all__'

class ProcedureForm(forms.ModelForm):
  class Meta:
    model = Procedure
    fields = '__all__'

class ProcedureApplicationForm(forms.ModelForm):
  class Meta:
    model = ProcedureApplication
    fields = '__all__'

class AssignMedicalStaffForm(forms.Form):
  medicalStaffId = forms.CharField()
  remove = forms.BooleanField(required=False)

class AppointmentForm(forms.ModelForm):
  class Meta:
    model = Appointment
    fields = '__all__'

class PrescriptionForm(forms.ModelForm):
  class Meta:
    model = Prescription
    fields = '__all__'