from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Patient, Doctor, PatientDoctor
from .serializers import PatientSerializer, DoctorSerializer, PatientDoctorDetailSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("You can only update your own patients.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("You can only delete your own patients.")
        return super().destroy(request, *args, **kwargs)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("You can only update your own doctors.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("You can only delete your own doctors.")
        return super().destroy(request, *args, **kwargs)

class PatientDoctorViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctor.objects.all()
    serializer_class = PatientDoctorDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, pk=None):
        mappings = PatientDoctor.objects.filter(patient_id=pk)
        if not mappings.exists():
            return Response({"detail": "No mappings found."}, status=404)
        
        serializer = PatientDoctorDetailSerializer(mappings, many=True)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
