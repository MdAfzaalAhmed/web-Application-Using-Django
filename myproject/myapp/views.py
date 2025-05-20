
# Create your views here.
from django.shortcuts import render,redirect
from .forms import FormSubmissionForm, ContactMessageForm
from .models import FormSubmission
def index(request):
    
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def form_view(request):
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Make sure 'index' URL name exists in urls.py
    else:
        form = FormSubmissionForm()
    return render(request, 'myapp/form.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ContactMessageForm()
    return render(request, 'myapp/contact.html', {'form': form})
