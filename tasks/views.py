# tasks/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def move_status(self, request, pk=None):
        """
        PATCH для изменения статуса (workflow).
        """
        task = self.get_object()
        status = request.data.get('status')
        notes = request.data.get('completion_notes', '')
        if status:
            task.status = status
            task.completion_notes = notes
            task.save()  # Триггерит signals
            return Response(TaskSerializer(task).data)
        return Response({'error': 'Status required'}, status=400)