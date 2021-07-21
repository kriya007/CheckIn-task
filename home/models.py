from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dob  = models.DateField()
    phone = models.CharField(max_length = 12)
    password = models.CharField(max_length=32)

    def __str__(self) :
        return self.name