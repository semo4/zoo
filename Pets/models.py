from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pet(models.Model):
    petName = models.CharField(max_length=100)
    petBirthdate = models.DateField()
    type = models.CharField(max_length=100)  # Dog/Cat/bird/etc...
    breed = models.CharField(max_length=100)
    petImage = models.CharField(max_length=2083)
    description = models.TextField(blank=True)


class Apply_adoption(models.Model):
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user_owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    approval_status = models.BooleanField(default=False)


class Adoption_by_user(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    petName = models.CharField(max_length=100)
    petBirthdate = models.DateField()
    type = models.CharField(max_length=100)  # Dog/Cat/bird/etc...
    breed = models.CharField(max_length=100)
    petImage = models.CharField(max_length=2083)
    description = models.TextField(blank=True)
