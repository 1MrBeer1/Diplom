from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.ReadOnlyField(source="project.name")
    created_by = serializers.ReadOnlyField(source="created_by.username")
    assigned_to_username = serializers.ReadOnlyField(source="assigned_to.username")

    class Meta:
        model = Task
        fields = "__all__"
