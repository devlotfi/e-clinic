from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import SearchForm, MedicalStaffForm
from ..models import MedicalStaff
from django.db.models import Q

# Create your views here.
@login_required(login_url='sign-in')
def addMedicalStaff(request: HttpRequest):
  form = MedicalStaffForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Medical Staff created successfully')
      return redirect('medical-staff-list')
  else:
    form = MedicalStaffForm()
  context = { 'form': form }
  return render(request, 'pages/medical-staff/add-medical-staff.html', context=context)

@login_required(login_url='sign-in')
def editMedicalStaff(request: HttpRequest, medicalStaffId: str):
  medicalStaff = get_object_or_404(MedicalStaff, id=medicalStaffId)
  form = MedicalStaffForm(instance=medicalStaff)
  if request.method == 'POST':
    form = MedicalStaffForm(data=request.POST, instance=medicalStaff)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Medical Staff updated successfully')
      return redirect('medical-staff-list')
  context = { 'form': form }
  return render(request, 'pages/medical-staff/edit-medical-staff.html', context=context)

@login_required(login_url='sign-in')
def deleteMedicalStaff(request: HttpRequest, medicalStaffId: str):
  medicalStaff = get_object_or_404(MedicalStaff, id=medicalStaffId)
  medicalStaff.delete()
  return redirect('medical-staff-list')

@login_required(login_url='sign-in')
def medicalStaffList(request: HttpRequest):
  form = SearchForm(request.GET)
  medicalStaffArray = []
  if form.is_valid():
    search = form.cleaned_data['search']
    medicalStaffArray = MedicalStaff.objects.filter(
      Q(id__icontains=search) |
      Q(department__name__icontains=search) |
      Q(speciality__name__icontains=search) |
      Q(firstName__icontains=search) |
      Q(lastName__icontains=search) |
      Q(dateOfBirth__icontains=search) |
      Q(address__icontains=search) |
      Q(phoneNumber__icontains=search) |
      Q(email__icontains=search) |
      Q(gender__icontains=search) |
      Q(updatedAt__icontains=search) |
      Q(createdAt__icontains=search) 
    )
  else:
    medicalStaffArray = MedicalStaff.objects.all()
  context = { 'medicalStaffArray': medicalStaffArray, 'form': form }
  return render(request, 'pages/medical-staff/medical-staff-list.html', context=context)