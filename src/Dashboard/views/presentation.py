from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from ..decorators import login_not_required
from ..models import Patient, MedicalStaff, Department, Speciality, Appointment, Genders

# Create your views here.
@login_not_required
def index(request: HttpRequest):
  return render(request, 'pages/presentation/index.html')

@login_required(login_url='sign-in')
def dashboard(request: HttpRequest):
  patientCount = Patient.objects.count()
  medicalStaffCount = MedicalStaff.objects.count()
  departmentCount = Department.objects.count()
  specialityCount = Speciality.objects.count()
  appointmentCount = Appointment.objects.count()

  departments = Department.objects.all()
  departmentMedicalStaffCount = {}
  for department in departments:
    medicalStaffCount = MedicalStaff.objects.filter(department=department.id).count()
    departmentMedicalStaffCount[department.name] = medicalStaffCount
  departmentMedicalStaffCountKeys = list(departmentMedicalStaffCount.keys())
  departmentMedicalStaffCountValues = list(departmentMedicalStaffCount.values())

  specialities = Speciality.objects.all()
  specialityMedicalStaffCount = {}
  for speciality in specialities:
    medicalStaffCount = MedicalStaff.objects.filter(speciality=speciality).count()
    specialityMedicalStaffCount[speciality.name] = medicalStaffCount
  specialityMedicalStaffCountKeys = list(specialityMedicalStaffCount.keys())
  specialityMedicalStaffCountValues = list(specialityMedicalStaffCount.values())

  patientCountByGender = {}
  patientMaleCount = Patient.objects.filter(gender=Genders.MALE).count()
  patientCountByGender['Male'] = patientMaleCount
  patientFemaleCount = Patient.objects.filter(gender=Genders.FEMALE).count()
  patientCountByGender['Female'] = patientFemaleCount
  patientCountByGenderKeys = list(patientCountByGender.keys())
  patientCountByGenderValues = list(patientCountByGender.values())

  medicalStaffCountByGender = {}
  medicalStaffMaleCount = MedicalStaff.objects.filter(gender=Genders.MALE).count()
  medicalStaffCountByGender['Male'] = medicalStaffMaleCount
  medicalStaffFemaleCount = MedicalStaff.objects.filter(gender=Genders.FEMALE).count()
  medicalStaffCountByGender['Female'] = medicalStaffFemaleCount
  medicalStaffCountByGenderKeys = list(medicalStaffCountByGender.keys())
  medicalStaffCountByGenderValues = list(medicalStaffCountByGender.values())

  context = {
    'patientCount': patientCount,
    'medicalStaffCount': medicalStaffCount,
    'departmentCount': departmentCount,
    'specialityCount': specialityCount,
    'appointmentCount': appointmentCount,

    'departmentMedicalStaffCountKeys': departmentMedicalStaffCountKeys,
    'departmentMedicalStaffCountValues': departmentMedicalStaffCountValues,

    'specialityMedicalStaffCountKeys': specialityMedicalStaffCountKeys,
    'specialityMedicalStaffCountValues': specialityMedicalStaffCountValues,

    'patientCountByGenderKeys': patientCountByGenderKeys,
    'patientCountByGenderValues': patientCountByGenderValues,

    'medicalStaffCountByGenderKeys': medicalStaffCountByGenderKeys,
    'medicalStaffCountByGenderValues': medicalStaffCountByGenderValues
  }
  return render(request, 'pages/presentation/dashboard-home.html', context=context)