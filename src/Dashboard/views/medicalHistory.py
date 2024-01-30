from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import MedicalHistoryForm
from ..models import Patient, MedicalHistory

# Create your views here.
@login_required(login_url='sign-in')
def editMedicalHistory(request: HttpRequest, patientId: str):
  patient = get_object_or_404(Patient, id=patientId)
  medicalHistory = get_object_or_404(MedicalHistory, patient=patient)
  form = MedicalHistoryForm(instance=medicalHistory, initial={'patient': patient})
  if request.method == 'POST':
    data = request.POST.copy() 
    data.appendlist('patient', patient)
    form = MedicalHistoryForm(data=data, instance=medicalHistory)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Medical history updated successfully')
      return redirect('patient-list')
  context = { 'form': form, 'patient': patient }
  return render(request, 'pages/medical-history/edit-medical-history.html', context=context)
