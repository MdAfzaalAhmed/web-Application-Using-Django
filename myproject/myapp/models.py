from django.db import models

# Create your models here.
from django.db import models

class FormSubmission(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    machines = models.CharField(max_length=100 ,null=True, blank=True) 

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField()
    your_message = models.TextField()

    def __str__(self):
        return self.your_name
