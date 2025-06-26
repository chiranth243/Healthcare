from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['user']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['user']

class PatientDoctorDetailSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    doctor_specialization = serializers.CharField(source='doctor.specialization', read_only=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), write_only=True)
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), write_only=True)

    class Meta:
        model = PatientDoctor
        fields = [
            'id', 'patient', 'doctor',  
            'patient_name', 'doctor_name', 'doctor_specialization'
        ]
        read_only_fields = ['user', 'patient_name', 'doctor_name', 'doctor_specialization']
