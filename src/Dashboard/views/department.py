from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import SearchForm, DepartmentForm
from ..models import Department
from django.db.models import Q

# Create your views here.
@login_required(login_url='sign-in')
def addDepartment(request: HttpRequest):
  form = DepartmentForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Department created successfully')
      return redirect('department-list')
  else:
    form = DepartmentForm()
  context = { 'form': form }
  return render(request, 'pages/department/add-department.html', context=context)

@login_required(login_url='sign-in')
def editDepartment(request: HttpRequest, departmentId: str):
  department = get_object_or_404(Department, id=departmentId)
  form = DepartmentForm(instance=department)
  if request.method == 'POST':
    form = DepartmentForm(data=request.POST, instance=department)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Department updated successfully')
      return redirect('department-list')
  context = { 'form': form }
  return render(request, 'pages/department/edit-department.html', context=context)

@login_required(login_url='sign-in')
def deleteDepartment(request: HttpRequest, departmentId: str):
  department = get_object_or_404(Department, id=departmentId)
  department.delete()
  return redirect('department-list')

@login_required(login_url='sign-in')
def departmentList(request: HttpRequest):
  form = SearchForm(request.GET)
  departments = []
  if form.is_valid():
    search = form.cleaned_data['search']
    departments = Department.objects.filter(
      Q(id__icontains=search) |
      Q(name__icontains=search)
    )
  else:
    departments = Department.objects.all()
  context = { 'departments': departments, 'form': form }
  return render(request, 'pages/department/department-list.html', context=context)