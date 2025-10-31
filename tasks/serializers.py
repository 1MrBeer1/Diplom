# tasks/serializers.py
from rest_framework import serializers
from .models import Task, KanbanColumn

class KanbanColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanColumn
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    assignee = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        """
        Валидация: При status='выполнена' — completion_notes required.
        """
        status = data.get('status')
        notes = data.get('completion_notes')
        if status == 'выполнена' and not notes:
            raise serializers.ValidationError("При сдаче на проверку укажите 'Что сделано'.")
        return data

    def update(self, instance, validated_data):
        status = validated_data.get('status')
        if status:
            instance.status = status
            instance.update_progress()  # Авто-progress
        return super().update(instance, validated_data)