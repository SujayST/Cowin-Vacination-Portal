from django.db import models
from django.forms.widgets import NullBooleanSelect
from django.utils import timezone
import datetime


# Create your models here.

class mRegister(models.Model):
    OPTIONS=(
        ('8:00am','8:00am'),
        ('10:00am','10:00am'),
        ('12:00pm','12:00pm'),
        ('2:00pm','2:00pm'),
    )
    Registration_id = models.AutoField(primary_key=True, serialize=True)
    Aadhar = models.BigIntegerField(unique=True)
    Name = models.CharField(max_length=20)
    Names = models.CharField(max_length=20)
    Phone = models.BigIntegerField(unique=True)
    Dob = models.DateField(default=timezone.now())
    PinCode = models.IntegerField(max_length=6)
    VSlot = models.CharField(max_length=20)
    VDate = models.DateField(default=timezone.now())
    
    
    def __str__(self):
        return self.Name