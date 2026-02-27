from django.db import models

class tbl_location(models.Model):
    location_name = models.CharField(max_length=50)
    doctor = models.ForeignKey('Guest.tbl_doctor', on_delete=models.CASCADE)
    available_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.IntegerField(default=1)
