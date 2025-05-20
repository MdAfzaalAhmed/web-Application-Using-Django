from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form_view, name='form'),
    path('contact/', views.contact, name='contact'),

]
