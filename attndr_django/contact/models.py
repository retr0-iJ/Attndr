from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255, null= True)
    email       = models.EmailField(max_length=255)
    subject     = models.CharField(max_length=255)
    message     = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'subject', 'message']