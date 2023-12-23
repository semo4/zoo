from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(verbose_name="User Name", max_length=1000)
    email = models.CharField(verbose_name="Email", max_length=1000)
    password = models.TextField(verbose_name="Password", max_length=1000)

    def __str__(self):
        return self.username
