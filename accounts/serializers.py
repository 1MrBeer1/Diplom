# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from .models import User

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для User: создание/редактирование (без пароля в output).
    При создании: генерирует username и пароль.
    """
    password = serializers.CharField(write_only=True, required=False)  # Для update
    generated_credentials = serializers.SerializerMethodField()  # Output: логин/пароль после create

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'department', 'password', 'generated_credentials']
        read_only_fields = ['id', 'generated_credentials']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def get_generated_credentials(self, obj):
        """
        Возвращает сгенерированные credentials (только после create).
        """
        if self.context.get('view').action == 'create':
            return {
                'username': obj.username,
                'temporary_password': self.context.get('temporary_password', 'Generated')
            }
        return None

    def create(self, validated_data):
        """
        Создание: генерирует username как 'user_{id}', пароль — random 12 chars.
        """
        # Генерация username (после создания, чтобы получить ID)
        temp_user = User.objects.create_user(
            email=validated_data['email'],
            role=validated_data.get('role', 'worker_design'),
            department=validated_data.get('department'),
            **{k: v for k, v in validated_data.items() if k != 'password'}
        )
        # Генерация пароля
        password = get_random_string(length=12)
        temp_user.set_password(password)
        temp_user.save()
        
        # Генерация username на основе ID
        temp_user.username = f"user_{temp_user.id}"
        temp_user.save()
        
        # Контекст для output
        self.context['temporary_password'] = password
        self.context['view'].action = 'create'  # Для get_generated_credentials
        
        return temp_user

    def update(self, instance, validated_data):
        """
        Update: обновляет поля, пароль — если передан (hashed).
        """
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_role(self, value):
        """
        Валидация: только разрешённые роли.
        """
        allowed_roles = [choice[0] for choice in User.ROLE_CHOICES]
        if value not in allowed_roles:
            raise serializers.ValidationError(f"Недопустимая роль: {value}. Доступны: {allowed_roles}")
        return value