from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, PatientDoctorViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)
router.register('mappings', PatientDoctorViewSet, basename='mappings')

urlpatterns = [
    path('', include(router.urls)),
    path('mappings/<int:pk>/', PatientDoctorViewSet.as_view({'get': 'retrieve'})),
]
