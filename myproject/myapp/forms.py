from django import forms
from .models import FormSubmission, ContactMessage

class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = '__all__'

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
