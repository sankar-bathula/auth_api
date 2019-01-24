from rest_framework.serializers import ModelSerializer
from auth_app_api.models import Employee
class EmployeeSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Employee
