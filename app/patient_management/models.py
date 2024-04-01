from django.db import models

# Create your models here.
class Patient(models.Model):
    """
    Represents a patient with basic personal information.
    
    Attributes:
        first_name (models.CharField): The patient's first name.
        last_name (models.CharField): The patient's last name.
        age (models.IntegerField): The patient's age. Uses IntegerField to store integer values.
        gender (models.CharField): The patient's gender. Stored as a CharField to accommodate custom gender identities.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)

    def __str__(self) -> str:
        """
        Returns a string representation of the Patient, which is the combination of
        the patient's first name and last name.
        
        Returns:
            str: A string that combines the patient's first name and last name.
        """
        return f"Patient: {self.first_name} {self.last_name}"

class Physician(models.Model):
    """
    Represents a physician with a specialty.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Physician: {self.first_name} {self.last_name}, {self.specialty}"

class MedicalProfile(models.Model):
    """
    Represents a medical profile linked to a specific patient.
    """
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
    diagnosis = models.CharField(max_length=255)
    current_medication = models.TextField()
    medical_images = models.TextField()

    def __str__(self) -> str:
        return f"Medical Profile for {self.patient}"

class Treatment(models.Model):
    """
    Represents a treatment relationship between a physician and a patient.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('patient', 'physician'),)

    def __str__(self) -> str:
        return f"Treatment: {self.patient} - {self.physician}"
