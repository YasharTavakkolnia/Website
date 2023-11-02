from django.db import models

class Contact (models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return f"{self.fullname} - {self.email}"
