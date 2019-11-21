from rest_framework import serializers
from v1.employees.models import Employee
from v1.users.serializers import UserSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['user', 'employee_id', 'store']

    def create(self, validated_data):
        return Employee.objects.signup(**validated_data)
