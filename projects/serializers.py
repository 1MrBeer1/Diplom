# projects/serializers.py
from rest_framework import serializers
from .models import Project, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = '__all__'