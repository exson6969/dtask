from rest_framework import serializers
from .models import Employee, VisitorLog

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'office_location', 'department']

class VisitorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorLog
        fields = ['id', 'visitor_name', 'visitor_email', 'visiting_employee', 'office_location', 'status']
