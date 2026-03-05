from django.db import models

# Create your models here.
class tbl_doctor(models.Model):
    doctor_name=models.CharField(max_length=20)
    doctor_contact=models.CharField(max_length=20)
    doctor_email=models.EmailField()
    doctor_gender=models.CharField(max_length=20)
    doctor_address=models.TextField()
    doctor_photo=models.FileField(upload_to='doctorDocs/')
    doctor_password=models.CharField(max_length=20)
   