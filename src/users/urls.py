from django.urls import path
from .views import CustomUserCreateView, LoginView, CustomUserDetailView

urlpatterns = [
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('<slug:user>/', CustomUserDetailView.as_view()),
]