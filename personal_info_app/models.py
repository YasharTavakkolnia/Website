from django.db import models

class Personalinfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birthday = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    instagram = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
