from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return  f'{self.username}'

class Motorcycle(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,)
    make =  models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100)
    plate = models.CharField(max_length=100 ,blank=True, null=True)

    def __str__(self):
        return  f'{self.plate}'

class Parking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    motor = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)