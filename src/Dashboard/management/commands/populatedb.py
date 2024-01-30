# myapp/management/commands/populate_data.py

from django.core.management.base import BaseCommand
from Dashboard.models import Department, Speciality, Procedure, ProcedureType, Patient, MedicalStaff, Genders, MedicalHistory
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **options):
      CardiologyDepartment = Department.objects.create(name="Cardiology")
      NeurologyDepartment = Department.objects.create(name="Neurology")
      UrologyDepartment = Department.objects.create(name="Urology")
      RheumatologyDepartment = Department.objects.create(name="Rheumatology")
      ENTDepartment = Department.objects.create(name="ENT")

      CardiologistSpeciality = Speciality.objects.create(name="Cardiologist")
      NeurologistSpeciality = Speciality.objects.create(name="Neurologist")
      UrologistSpeciality = Speciality.objects.create(name="Urologist")
      RheumatologistSpeciality = Speciality.objects.create(name="Rheumatologist")
      ENTSpeciality = Speciality.objects.create(name="ENT")
      GeneralistSpeciality = Speciality.objects.create(name="Generalist")
      NurseSpeciality = Speciality.objects.create(name="Nurse")

      Procedure.objects.create(name = "Cardiologist consultation", type=ProcedureType.MEDICAL, department=CardiologyDepartment)
      Procedure.objects.create(name = "Heart surgery", type=ProcedureType.MEDICAL, department=CardiologyDepartment)
      Procedure.objects.create(name = "Blood test", type=ProcedureType.MEDICAL, department=CardiologyDepartment)

      Procedure.objects.create(name = "Neurologist consultation", type=ProcedureType.MEDICAL, department=NeurologyDepartment)
      Procedure.objects.create(name = "Urologist consultation", type=ProcedureType.MEDICAL, department=UrologyDepartment)
      Procedure.objects.create(name = "Rheumatologist consultation", type=ProcedureType.MEDICAL, department=RheumatologyDepartment)
      Procedure.objects.create(name = "ENT consultation", type=ProcedureType.MEDICAL, department=ENTDepartment)

      patient1 = Patient.objects.create(
        firstName='patient1',
        lastName='patient1',
        dateOfBirth='2004-06-18',
        address='Address of patient1',
        phoneNumber='0500000001',
        email='patient1@patient1.com',
        gender=Genders.MALE
      )
      MedicalHistory.objects.create(patient=patient1)
      patient2 = Patient.objects.create(
        firstName='patient2',
        lastName='patient2',
        dateOfBirth='2004-06-18',
        address='Address of patient2',
        phoneNumber='0500000002',
        email='patient2@patient2.com',
        gender=Genders.FEMALE
      )
      MedicalHistory.objects.create(patient=patient2)
      patient3 = Patient.objects.create(
        firstName='patient3',
        lastName='patient3',
        dateOfBirth='2004-06-18',
        address='Address of patient3',
        phoneNumber='0500000003',
        email='patient3@patient3.com',
        gender=Genders.MALE
      )
      MedicalHistory.objects.create(patient=patient3)
      patient4 = Patient.objects.create(
        firstName='patient4',
        lastName='patient4',
        dateOfBirth='2004-06-18',
        address='Address of patient4',
        phoneNumber='0500000004',
        email='patient4@patient4.com',
        gender=Genders.FEMALE
      )
      MedicalHistory.objects.create(patient=patient4)
      patient5 = Patient.objects.create(
        firstName='patient5',
        lastName='patient5',
        dateOfBirth='2004-06-18',
        address='Address of patient5',
        phoneNumber='0500000005',
        email='patient5@patient5.com',
        gender=Genders.MALE
      )
      MedicalHistory.objects.create(patient=patient5)

      MedicalStaff.objects.create(
        department=CardiologyDepartment,
        speciality=CardiologistSpeciality,
        firstName='medicalstaff1',
        lastName='medicalstaff1',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff1',
        phoneNumber='0500000001',
        email='medicalstaff1@medicalstaff1.com',
        gender=Genders.MALE
      )
      MedicalStaff.objects.create(
        department=NeurologyDepartment,
        speciality=NeurologistSpeciality,
        firstName='medicalstaff2',
        lastName='medicalstaff2',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff2',
        phoneNumber='0500000002',
        email='medicalstaff2@medicalstaff2.com',
        gender=Genders.MALE
      )
      MedicalStaff.objects.create(
        department=UrologyDepartment,
        speciality=UrologistSpeciality,
        firstName='medicalstaff3',
        lastName='medicalstaff3',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff3',
        phoneNumber='0500000003',
        email='medicalstaff3@medicalstaff3.com',
        gender=Genders.MALE
      )
      MedicalStaff.objects.create(
        department=RheumatologyDepartment,
        speciality=RheumatologistSpeciality,
        firstName='medicalstaff4',
        lastName='medicalstaff4',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff4',
        phoneNumber='0500000004',
        email='medicalstaff4@medicalstaff4.com',
        gender=Genders.FEMALE
      )
      MedicalStaff.objects.create(
        department=ENTDepartment,
        speciality=ENTSpeciality,
        firstName='medicalstaff5',
        lastName='medicalstaff5',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff5',
        phoneNumber='0500000005',
        email='medicalstaff5@medicalstaff5.com',
        gender=Genders.FEMALE
      )
      MedicalStaff.objects.create(
        department=CardiologyDepartment,
        speciality=NurseSpeciality,
        firstName='medicalstaff6',
        lastName='medicalstaff6',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff6',
        phoneNumber='0500000006',
        email='medicalstaff6@medicalstaff6.com',
        gender=Genders.MALE
      )
      MedicalStaff.objects.create(
        department=CardiologyDepartment,
        speciality=GeneralistSpeciality,
        firstName='medicalstaff7',
        lastName='medicalstaff7',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff7',
        phoneNumber='0500000007',
        email='medicalstaff7@medicalstaff7.com',
        gender=Genders.MALE
      )
      MedicalStaff.objects.create(
        department=NeurologyDepartment,
        speciality=NeurologistSpeciality,
        firstName='medicalstaff8',
        lastName='medicalstaff8',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff8',
        phoneNumber='0500000008',
        email='medicalstaff8@medicalstaff8.com',
        gender=Genders.FEMALE
      )
      MedicalStaff.objects.create(
        department=ENTDepartment,
        speciality=NurseSpeciality,
        firstName='medicalstaff9',
        lastName='medicalstaff9',
        dateOfBirth='2004-06-18',
        address='Address of medicalstaff9',
        phoneNumber='0500000009',
        email='medicalstaff9@medicalstaff9.com',
        gender=Genders.MALE
      )

      User.objects.create_superuser(
        username='admin',
        email='admin@admin.com',
        password='admin'
      )

      self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
