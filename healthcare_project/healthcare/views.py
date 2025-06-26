from rest_framework import viewsets, permissions
from .models import Patient, Doctor, PatientDoctor
from .serializers import PatientSerializer, DoctorSerializer, PatientDoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all() 
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctor.objects.all()
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
