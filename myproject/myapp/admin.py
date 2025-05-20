from django.contrib import admin
from .models import FormSubmission, ContactMessage

# Register your models here.
admin.site.register(FormSubmission)
admin.site.register(ContactMessage)