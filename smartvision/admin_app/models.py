from django.db import models

# Create your models here.
from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='admin/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=100)

    def __str__(self):
        return self.place_name
