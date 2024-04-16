from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .models import Patient, Physician, Treatment, MedicalProfile
# Create your views here.

log_data = 'log_data/'
search = 'search/'


class HomeView(TemplateView):
    template_name = 'home.html' 

class PatientView(CreateView):
    model = Patient
    fields = '__all__'
    template_name = f'{log_data}patients.html'
    success_url = '/success/'

    # def get(self, request):
    #     form = Patient
    #     return render(request, self.template_name, context={'form' : form} ) 

    # def post(self, request):
    #     form = Patient(request.POST)
    #     if form.is_valid():
    #         print(form)


class PhysicianView(CreateView):
    model  = Physician
    fields = '__all__'
    template_name = f'{log_data}physician.html'
    success_url = '/success/'


class MedicalProfileView(CreateView):
    model  = MedicalProfile
    fields = '__all__'
    template_name = f'{log_data}medical-profile.html'
    success_url = '/success/'


class TreatmentView(CreateView):
    model  = Treatment
    fields = '__all__'
    template_name = f'{log_data}treatment.html'
    success_url = '/success/'

    
class SuccessView(TemplateView):
    template_name = f"{log_data}success.html"
    

class SampleData(TemplateView):
    template_name = f'{log_data}sample_data.html'



class PatientsSearchView(ListView):
    model = Patient
    template_name = f'{search}search-patients.html'
    context_object_name = 'patients'

    def get_queryset(self):
        queryset = super().get_queryset()
        first_name_query = self.request.GET.get('first_name', '')
        last_name_query = self.request.GET.get('last_name', '')
        gender_query = self.request.GET.get('gender', '')

        if first_name_query or last_name_query or gender_query:
            queryset = queryset.filter(
                first_name__icontains=first_name_query,
                last_name__icontains=last_name_query,
                gender__iexact=gender_query
            )
        else:
            return Patient.objects.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_performed'] = bool(self.request.GET)  # Checks if any GET request exists
        context['first_name_query'] = self.request.GET.get('first_name', '')
        context['last_name_query'] = self.request.GET.get('last_name', '')
        context['gender_query'] = self.request.GET.get('gender', '')
        return context
    

class PhysicianSearchView(ListView):
    model = Physician
    template_name = f'{search}search-physicians.html'
    context_object_name = 'physicians'

    def get_queryset(self):
        # Start with an empty queryset
        queryset = Physician.objects.none()

        # Get search parameters from the request
        first_name_query = self.request.GET.get('first_name', '')
        last_name_query = self.request.GET.get('last_name', '')
        specialty_query = self.request.GET.get('specialty', '')

        # Check if any search parameter has been provided
        if first_name_query or last_name_query or (specialty_query and specialty_query != "All"):
            queryset = Physician.objects.all()  # Get the full queryset to apply filters

            if first_name_query:
                queryset = queryset.filter(first_name__icontains=first_name_query)
            if last_name_query:
                queryset = queryset.filter(last_name__icontains=last_name_query)
            if specialty_query and specialty_query != "All":
                queryset = queryset.filter(specialty__iexact=specialty_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialty_query'] = self.request.GET.get('specialty', 'All')
        context['all_specialties'] = ['All'] + list(Physician.objects.values_list('specialty', flat=True).distinct())
        # Add a flag to check if a search has been performed
        context['search_performed'] = bool(self.request.GET)
        return context 


class TreatmentSearchView(ListView):
    model = Treatment
    template_name = f'{search}search-treatment.html'
    context_object_name = 'treatments'

    def get_queryset(self):
        queryset = super().get_queryset()
        patient_query = self.request.GET.get('patient', '')
        physician_query = self.request.GET.get('physician', '')

        if patient_query:
            queryset = queryset.filter(patient__first_name__icontains=patient_query) | queryset.filter(patient__last_name__icontains=patient_query)
        if physician_query:
            queryset = queryset.filter(physician__first_name__icontains=physician_query) | queryset.filter(physician__last_name__icontains=physician_query)

        return queryset
