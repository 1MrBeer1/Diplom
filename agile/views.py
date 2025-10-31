from django.shortcuts import render

# Create your views here.
# agile/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Sprint
from .serializers import SprintSerializer  # Создай аналогично выше

class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

    @action(detail=True)
    def burndown(self, request, pk=None):
        sprint = self.get_object()
        data = sprint.calculate_burndown_data()
        return Response(data)