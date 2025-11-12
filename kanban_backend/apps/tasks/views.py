from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Возвращаем все задачи по проекту, сгруппированные по колонкам
    @action(detail=False, methods=["get"], url_path="kanban/(?P<project_id>[^/.]+)")
    def kanban_view(self, request, project_id=None):
        tasks = Task.objects.filter(project_id=project_id).order_by("order")
        columns = {status: [] for status, _ in Task.Status.choices}
        for task in tasks:
            columns[task.column].append(TaskSerializer(task).data) # type: ignore
        return Response(columns)

    # Массовое обновление позиций и колонок
    @action(detail=False, methods=["patch"], url_path="bulk-update")
    def bulk_update(self, request):
        """
        При drag & drop фронт присылает массив:
        [
            {"id": 5, "column": "IN_PROGRESS", "order": 0},
            {"id": 8, "column": "IN_PROGRESS", "order": 1},
            {"id": 9, "column": "TODO", "order": 0}
        ]
        """
        updates = request.data
        for item in updates:
            try:
                task = Task.objects.get(pk=item["id"])
                task.column = item["column"]
                task.order = item["order"]
                task.save()
            except Task.DoesNotExist:
                continue
        return Response({"status": "updated"}, status=status.HTTP_200_OK)
