from rest_framework import serializers
from .models import Project
from apps.tasks.models import Task

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        project = Project.objects.create(created_by=user, **validated_data)
        # автоматическое создание базовой задачи
        Task.objects.create(
            project=project,
            title="Initial SEO review",
            created_by=user,
            assigned_to=user,
            department="SEO"
        )
        return project
