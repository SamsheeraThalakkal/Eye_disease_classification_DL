from django.db import models

# Create your models here.

class tbl_patient(models.Model):
    patient_name=models.CharField(max_length=20)
    patient_contact=models.CharField(max_length=20)
    patient_email=models.EmailField()
    patient_gender=models.CharField(max_length=20)
    patient_address=models.TextField()
    patient_photo=models.FileField(upload_to='patientDocs/')
  
    patient_password=models.CharField(max_length=20)
    patient_status=models.IntegerField(default=0)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=20)
    admin_password=models.CharField(max_length=20)

