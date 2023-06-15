from django.db import models
import datetime as dt
# Create your models here.


class Appoitment(models.Model):

    server = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    appoitment_data = models.DateField()
    appoitment_time = models.TimeField()
    def __str__(self):
        return self.name

