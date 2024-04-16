from django.urls import path 

from .views import *

urlpatterns = [
    
    # home-session
    path('', HomeView.as_view(), name="home"),

    path('patient/',  PatientView.as_view(), name="patient"),
    path('physician/', PhysicianView.as_view(), name="physician"),
    path('medical-profile/', MedicalProfileView.as_view(), name="medical-profile"),
    path('treatment/', TreatmentView.as_view(), name="treatment"),
    path('sample-data', SampleData.as_view(), name='sample-data'),
    path('success/', SuccessView.as_view(), name="success"),

    # SEARCH FUNCTIONALITY
    path('search-patients/', PatientsSearchView.as_view(), name='search-patients'),
    path('search-physicians/', PhysicianSearchView.as_view(), name='search-physicians'),
    path('search-treatement/', TreatmentSearchView.as_view(), name='search-treatment'),
    path('search-medical-profile/', TreatmentSearchView.as_view(), name='search-medical-profile'),
]
