from django.urls import path
from .views import medicalStaff, presentation, auth, patient, medicalHistory, department, procedure, speciality, appointement, procedureApplication, prescription

urlpatterns = [
  path('', presentation.index, name='index'),
  path('dashboard', presentation.dashboard, name='dashboard'),

  path('auth/sign-in/', auth.signIn, name='sign-in'),
  path('auth/sign-out/', auth.signOut, name='sign-out'),
  path('auth/users/', auth.userList, name='user-list'),
  path('auth/users/add/', auth.addUser, name='add-user'),
  path('auth/users/edit/<str:userId>/', auth.editUser, name='edit-user'),
  path('auth/users/delete/<str:userId>/', auth.deleteUser, name='delete-user'),

  path('dashboard/patients/', patient.patientList, name='patient-list'),
  path('dashboard/patients/add/', patient.addPatient, name='add-patient'),
  path('dashboard/patients/edit/<str:patientId>/', patient.editPatient, name='edit-patient'),
  path('dashboard/patients/delete/<str:patientId>/', patient.deletePatient, name='delete-patient'),

  path('dashboard/patients/edit/<str:patientId>/history/', medicalHistory.editMedicalHistory, name='edit-medical-history'),

  path('dashboard/medical-staff/', medicalStaff.medicalStaffList, name='medical-staff-list'),
  path('dashboard/medical-staff/add/', medicalStaff.addMedicalStaff, name='add-medical-staff'),
  path('dashboard/medical-staff/edit/<str:medicalStaffId>/', medicalStaff.editMedicalStaff, name='edit-medical-staff'),
  path('dashboard/medical-staff/delete/<str:medicalStaffId>/', medicalStaff.deleteMedicalStaff, name='delete-medical-staff'),

  path('dashboard/departments/', department.departmentList, name='department-list'),
  path('dashboard/departments/add/', department.addDepartment, name='add-department'),
  path('dashboard/departments/edit/<str:departmentId>/', department.editDepartment, name='edit-department'),
  path('dashboard/departments/delete/<str:departmentId>/', department.deleteDepartment, name='delete-department'),

  path('dashboard/specialities/', speciality.specialityList, name='speciality-list'),
  path('dashboard/specialities/add/', speciality.addSpeciality, name='add-speciality'),
  path('dashboard/specialities/edit/<str:specialityId>/', speciality.editSpeciality, name='edit-speciality'),
  path('dashboard/specialities/delete/<str:specialityId>/', speciality.deleteSpeciality, name='delete-speciality'),

  path('dashboard/procedures/', procedure.procedureList, name='procedure-list'),
  path('dashboard/procedures/add/', procedure.addProcedure, name='add-procedure'),
  path('dashboard/procedures/edit/<str:procedureId>/', procedure.editProcedure, name='edit-procedure'),
  path('dashboard/procedures/delete/<str:procedureId>/', procedure.deleteProcedure, name='delete-procedure'),

  path('dashboard/appointments/patient/<str:patientId>/add/', appointement.addAppointement, name='add-appointment'),
  path('dashboard/appointments/edit/<str:appointmentId>/', appointement.editAppointment, name='edit-appointment'),
  path('dashboard/appointments/patient/<str:patientId>/', appointement.appointmentListPatient, name='appointment-list-patient'),
  path('dashboard/appointments/medical-staff/<str:medicalStaffId>/', appointement.appointmentListMedicalStaff, name='appointment-list-medical-staff'),
  path('dashboard/appointments/delete/<str:appointmentId>/', appointement.deleteAppointment, name='delete-appointment'),
  path('dashboard/appointments/apply-procedure/<str:appointmentId>/', procedureApplication.applyProcedure, name='apply-procedure'),

  path('dashboard/procedure-applications/delete/<str:procedureApplicationId>/', procedureApplication.deleteProcedureApplication, name='delete-procedure-application'),

  path('dashboard/prescriptions/patient/<str:appointmentId>/add/', prescription.addPrescription, name='add-prescription'),
  path('dashboard/prescriptions/patient/<str:prescriptionId>/edit/', prescription.editPrescription, name='edit-prescription'),
  path('dashboard/prescriptions/patient/<str:prescriptionId>/delete/', prescription.deletePrescription, name='delete-prescription'),
]
