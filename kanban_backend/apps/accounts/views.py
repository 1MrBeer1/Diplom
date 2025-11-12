from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

# /api/auth/me/
class MeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
