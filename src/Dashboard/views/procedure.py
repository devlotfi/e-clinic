from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import SearchForm, ProcedureForm
from ..models import Procedure
from django.db.models import Q

# Create your views here.
@login_required(login_url='sign-in')
def addProcedure(request: HttpRequest):
  form = ProcedureForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Procedure created successfully')
      return redirect('procedure-list')
  else:
    form = ProcedureForm()
  context = { 'form': form }
  return render(request, 'pages/procedure/add-procedure.html', context=context)

@login_required(login_url='sign-in')
def editProcedure(request: HttpRequest, procedureId: str):
  procedure = get_object_or_404(Procedure, id=procedureId)
  form = ProcedureForm(instance=procedure)
  if request.method == 'POST':
    form = ProcedureForm(data=request.POST, instance=procedure)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Procedure updated successfully')
      return redirect('procedure-list')
  context = { 'form': form }
  return render(request, 'pages/procedure/edit-procedure.html', context=context)

@login_required(login_url='sign-in')
def deleteProcedure(request: HttpRequest, procedureId: str):
  procedure = get_object_or_404(Procedure, id=procedureId)
  procedure.delete()
  return redirect('procedure-list')

@login_required(login_url='sign-in')
def procedureList(request: HttpRequest):
  form = SearchForm(request.GET)
  procedures = []
  if form.is_valid():
    search = form.cleaned_data['search']
    procedures = Procedure.objects.filter(
      Q(id__icontains=search) |
      Q(name__icontains=search)
    )
  else:
    procedures = Procedure.objects.all()
  context = { 'procedures': procedures, 'form': form }
  return render(request, 'pages/procedure/procedure-list.html', context=context)