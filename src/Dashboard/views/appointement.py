from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import AppointmentForm, SearchForm
from ..models import Patient, Appointment, MedicalStaff, ProcedureApplication, Prescription
from django.db.models import Q

@login_required(login_url='sign-in')
def addAppointement(request: HttpRequest, patientId: str):
  patient = get_object_or_404(Patient, id=patientId)
  form = AppointmentForm(initial={'patient': patient})
  if request.method == 'POST':
    data = request.POST.copy() 
    data.appendlist('patient', patient)
    form = AppointmentForm(data=data)
    if form.is_valid():
      appointment = form.save()
      messages.success(request=request, message='Appointment created successfully')
      return redirect('edit-appointment', appointmentId=appointment.id)
  context = { 'form': form, 'patient': patient }
  return render(request, 'pages/appointment/add-appointment.html', context=context)

@login_required(login_url='sign-in')
def editAppointment(request: HttpRequest, appointmentId: str):
  appointment = get_object_or_404(Appointment, id=appointmentId)
  patient = get_object_or_404(Patient, id=appointment.patient.id)
  procedureApplications = ProcedureApplication.objects.filter(appointment=appointment.id).order_by('procedure')
  prescriptions = Prescription.objects.filter(appointment=appointment)

  form = AppointmentForm(instance=appointment, initial={'patient': patient})
  if request.method == 'POST':
    data = request.POST.copy() 
    data.appendlist('patient', patient)
    form = AppointmentForm(data=data, instance=appointment)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Appointment updated successfully')
      return redirect('appointment-list-patient', patientId=patient.id)
  context = { 'form': form, 'patient': patient, 'procedureApplications': procedureApplications, 'prescriptions': prescriptions, 'appointment': appointment }
  return render(request, 'pages/appointment/edit-appointment.html', context=context)

@login_required(login_url='sign-in')
def deleteAppointment(request: HttpRequest, appointmentId: str):
  appointment = get_object_or_404(Appointment, id=appointmentId)
  patient = appointment.patient
  appointment.delete()
  return redirect('appointment-list-patient', patientId=patient.id)

@login_required(login_url='sign-in')
def appointmentListMedicalStaff(request: HttpRequest, medicalStaffId: str):
  medicalStaff = get_object_or_404(MedicalStaff, id=medicalStaffId)

  procedure_applications_for_medical_staff = ProcedureApplication.objects.filter(medicalStaff=medicalStaff)
  appointments_for_medical_staff = [pa.appointment for pa in procedure_applications_for_medical_staff]

  length = len(appointments_for_medical_staff)

  context = { 'appointments': appointments_for_medical_staff, 'medicalStaff': medicalStaff, 'length': length }
  return render(request, 'pages/appointment/appointment-list-medical-staff.html', context=context)

@login_required(login_url='sign-in')
def appointmentListPatient(request: HttpRequest, patientId: str):
  patient = get_object_or_404(Patient, id=patientId)
  form = SearchForm(request.GET)
  appointments = []
  if form.is_valid():
    search = form.cleaned_data['search']
    appointments = Appointment.objects.filter(
      Q(id__icontains=search) |
      Q(timestamp__icontains=search) |
      Q(state__icontains=search),
      patient=patient,
    ).order_by('-timestamp')
  else:
    appointments = Appointment.objects.filter(
      patient=patient,
    ).order_by('-timestamp')
  context = { 'appointments': appointments, 'form': form, 'patient': patient }
  return render(request, 'pages/appointment/appointment-list-patient.html', context=context)