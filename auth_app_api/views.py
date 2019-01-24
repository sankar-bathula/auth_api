from django.shortcuts import render
from auth_app_api.models import Employee
from auth_app_api.serializer import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from auth_app_api.permissions import IsReadOnlyPermissions, SunnyPermissions
# Create your views here.
class EmployeeCRUDAPI(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    authentication_classes = [ TokenAuthentication,]
    permission_classes = [SunnyPermissions,]
