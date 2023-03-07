from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ad:")
    last_name = models.CharField(max_length=100, verbose_name="Soyad:")
    email = models.EmailField(max_length=100, verbose_name="E-poçt adresi:")
    phone = models.CharField(max_length=100, verbose_name="Telefon:")
    message = models.TextField(blank=True, verbose_name="Mesaj:")

    def __str__(self):
        return self.email