from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import AppointmentForm, SearchForm, ProcedureApplicationForm, AssignMedicalStaffForm
from ..models import Patient, Appointment, MedicalStaff, ProcedureApplication
from django.db.models import Q

@login_required(login_url='sign-in')
def applyProcedure(request: HttpRequest, appointmentId: str):
  appointment = get_object_or_404(Appointment, id=appointmentId)
  patient = get_object_or_404(Patient, id=appointment.patient.id)
  form = ProcedureApplicationForm(initial={'appointment': appointment})
  searchForm = SearchForm(request.GET)
  assignMedicalStaffForm = AssignMedicalStaffForm(request.POST)
  medicalStaff = None
  medicalStaffList = []

  if request.method == 'POST':
    if request.POST.get('confirm'):
      data = request.POST.copy() 
      data.appendlist('appointment', appointment)
      form = ProcedureApplicationForm(data=data)
      if form.is_valid():
        form.save()
        messages.success(request=request, message='Procedure applied successfully')
        return redirect('edit-appointment', appointmentId=appointment.id)
    else:
      if assignMedicalStaffForm.is_valid():
        if assignMedicalStaffForm.cleaned_data['remove']:
          medicalStaff = None
        else:
          medicalStaff = get_object_or_404(MedicalStaff, id=assignMedicalStaffForm.cleaned_data['medicalStaffId'])
  
  if searchForm.is_valid():
    search = searchForm.cleaned_data['search']
    if search:
      medicalStaffList = MedicalStaff.objects.filter(
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
      medicalStaffList = MedicalStaff.objects.all()

  print(medicalStaff)
  context = { 'form': form, 'searchForm': searchForm, 'assignMedicalStaffForm': AssignMedicalStaffForm(), 'removeMedicalStaffForm': AssignMedicalStaffForm(), 'patient': patient, 'appointment': appointment, 'medicalStaff': medicalStaff, 'medicalStaffList': medicalStaffList }
  return render(request, 'pages/procedure-application/apply-procedure.html', context=context)

@login_required(login_url='sign-in')
def deleteProcedureApplication(request: HttpRequest, procedureApplicationId: str):
  procedureApplication = get_object_or_404(ProcedureApplication, id=procedureApplicationId)
  appointment = procedureApplication.appointment
  procedureApplication.delete()
  messages.success(request=request, message='Procedure application deleted successfully')
  return redirect('edit-appointment', appointmentId=appointment.id)