from django.db import models

# Create your models here.

class UsersInputModel(models.Model):
    houseHold_Number = models.IntegerField()
    Residence_Country = models.CharField(max_length=65)
    housing_Size = models.IntegerField()
    housing_Type = models.CharField(max_length=65)
    daily_Electricity_Consumption = models.IntegerField()
    energy_Source = models.CharField(max_length=65)

