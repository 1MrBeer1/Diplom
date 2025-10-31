# accounts/permissions.py
from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

User = get_user_model()

class IsSEOOrAdminPermission(BasePermission):
    """
    Разрешает доступ только пользователям с ролью 'seo' или 'admin'.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['seo', 'admin']
    
    def has_object_permission(self, request, view, obj):
        # Для update/delete: seo/admin может редактировать/удалять любого
        return self.has_permission(request, view)