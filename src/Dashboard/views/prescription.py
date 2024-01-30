from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import SearchForm, PrescriptionForm
from ..models import Prescription, Appointment, Patient
from django.db.models import Q

# Create your views here.
@login_required(login_url='sign-in')
def addPrescription(request: HttpRequest, appointmentId: str):
  appointment = get_object_or_404(Appointment, id=appointmentId)
  patient = appointment.patient
  form = PrescriptionForm(initial={'appointment': appointment})
  if request.method == 'POST':
    data = request.POST.copy() 
    data.appendlist('appointment', appointment)
    form = PrescriptionForm(data=data)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Prescription created successfully')
      return redirect('edit-appointment', appointmentId=appointment.id)
  context = { 'form': form, 'patient': patient, 'appointment': appointment }
  return render(request, 'pages/prescription/add-prescription.html', context=context)

@login_required(login_url='sign-in')
def editPrescription(request: HttpRequest, prescriptionId: str):
  prescription = get_object_or_404(Prescription, id=prescriptionId)
  appointment = get_object_or_404(Appointment, id=prescription.appointment.id)
  patient = get_object_or_404(Patient, id=appointment.patient.id)

  form = PrescriptionForm(instance=prescription, initial={'patient': patient})
  if request.method == 'POST':
    data = request.POST.copy() 
    data.appendlist('appointment', appointment)
    form = PrescriptionForm(data=data, instance=prescription)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Prescription updated successfully')
      return redirect('edit-appointment', appointmentId=appointment.id)
  context = { 'form': form, 'patient': patient, 'appointment': appointment }
  return render(request, 'pages/prescription/edit-prescription.html', context=context)

@login_required(login_url='sign-in')
def deletePrescription(request: HttpRequest, prescriptionId: str):
  prescription = get_object_or_404(Prescription, id=prescriptionId)
  appointment = get_object_or_404(Appointment, id=prescription.appointment.id)
  prescription.delete()
  return redirect('edit-appointment', appointmentId=appointment.id)