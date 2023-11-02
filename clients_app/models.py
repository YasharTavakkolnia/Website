from django.db import models

class Client(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='clients')

    def __str__(self):
        return self.title