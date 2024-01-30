from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import SearchForm, SpecialityForm
from ..models import Speciality
from django.db.models import Q

# Create your views here.
@login_required(login_url='sign-in')
def addSpeciality(request: HttpRequest):
  form = SpecialityForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Speciality created successfully')
      return redirect('speciality-list')
  else:
    form = SpecialityForm()
  context = { 'form': form }
  return render(request, 'pages/speciality/add-speciality.html', context=context)

@login_required(login_url='sign-in')
def editSpeciality(request: HttpRequest, specialityId: str):
  speciality = get_object_or_404(Speciality, id=specialityId)
  form = SpecialityForm(instance=speciality)
  if request.method == 'POST':
    form = SpecialityForm(data=request.POST, instance=speciality)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Speciality updated successfully')
      return redirect('speciality-list')
  context = { 'form': form }
  return render(request, 'pages/speciality/edit-speciality.html', context=context)

@login_required(login_url='sign-in')
def deleteSpeciality(request: HttpRequest, specialityId: str):
  speciality = get_object_or_404(Speciality, id=specialityId)
  speciality.delete()
  return redirect('speciality-list')

@login_required(login_url='sign-in')
def specialityList(request: HttpRequest):
  form = SearchForm(request.GET)
  specialities = []
  if form.is_valid():
    search = form.cleaned_data['search']
    specialities = Speciality.objects.filter(
      Q(id__icontains=search) |
      Q(name__icontains=search)
    )
  else:
    specialities = Speciality.objects.all()
  context = { 'specialities': specialities, 'form': form }
  return render(request, 'pages/speciality/speciality-list.html', context=context)