# accounts/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend  # Теперь доступен
from django.utils.crypto import get_random_string
from .models import User
from .serializers import UserSerializer
from .permissions import IsSEOOrAdminPermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Добавлено для basename в router
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsSEOOrAdminPermission]
    filter_backends = [DjangoFilterBackend]  # Для фильтрации
    filterset_fields = ['role', 'department']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsSEOOrAdminPermission]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'user': UserSerializer(user).data,
                'message': 'Пользователь создан. Уведомите сотрудника о credentials.',
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            from rest_framework_simplejwt.tokens import RefreshToken
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def refresh(self, request):
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = request.data.get('refresh')
        try:
            token = RefreshToken(refresh)
            return Response({'access': str(token.access_token)})
        except:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=True, methods=['post'], permission_classes=[IsSEOOrAdminPermission])
    def reset_password(self, request, pk=None):
        user = self.get_object()
        new_password = get_random_string(length=12)
        user.set_password(new_password)
        user.save()
        return Response({
            'message': 'Пароль сброшен.',
            'temporary_password': new_password  # В prod: не возвращать, только email
        })