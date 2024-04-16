from django.urls import path 
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    
    # home-session
    path('', HomeView.as_view(), name="home"),

    path('patient/create/',  PatientView.as_view(), name="patient"),
    path('physician/create/', PhysicianView.as_view(), name="physician"),
    path('medical-profile/create/', MedicalProfileView.as_view(), name="medical-profile"),
    path('treatment/create/', TreatmentView.as_view(), name="treatment"),
    path('sample-data', SampleData.as_view(), name='sample-data'),
    path('success/', SuccessView.as_view(), name="success"),

    # SEARCH FUNCTIONALITY
    path('search-patients/', PatientsSearchView.as_view(), name='search-patients'),
    path('search-physicians/', PhysicianSearchView.as_view(), name='search-physicians'),
    path('search-treatement/', TreatmentSearchView.as_view(), name='search-treatment'),
    path('search-medical-profile/', TreatmentSearchView.as_view(), name='search-medical-profile'),

    # 
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
