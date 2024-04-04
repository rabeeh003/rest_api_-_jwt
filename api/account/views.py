
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import UserLoginSerializer, UserRegistrationSerializer

User = get_user_model()

class UserRegistrationView(CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        serializer.save()

class LoginView(CreateAPIView):
    serializer_class = UserLoginSerializer