from django.urls import path
from .views import CustomUserCreateView, LoginView

urlpatterns = [
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login')
]