
from django.urls import path
from .views import UserRegistrationView, LoginView
urlpatterns = [
    path('register/', UserRegistrationView.as_view() ),
    path('login/', LoginView.as_view() ),
]
