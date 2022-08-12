from django.urls import path
from .views import SponsorCreateView, SponsorsListView, SponsorDetailView, StudentCreateView, StudentDetailView, \
    UniversityListCreateView, UniversityDetailView, StudentListView, StudentAboutView, SponsorsOfStudentView, \
    SponsorsAddStudentView, SponsorsOfStudentDetailView, DashboardView

urlpatterns = [
    path('', SponsorCreateView.as_view()),
    path('sponsor/all/', SponsorsListView.as_view()),
    path('sponsor/<int:id>/', SponsorDetailView.as_view()),
    path('university/', UniversityListCreateView.as_view()),
    path('university/<int:id>/', UniversityDetailView.as_view()),
    path('student/create/', StudentCreateView.as_view()),
    path('student/<int:id>/', StudentDetailView.as_view()),
    path('student/all/', StudentListView.as_view()),
    path('student/about/<int:id>/', StudentAboutView().as_view()),
    path('student/<int:id>/sponsors/', SponsorsOfStudentView.as_view()),
    path('student/add/<int:id>/', SponsorsAddStudentView.as_view()),
    path('sponsor/student/<int:id>/', SponsorsOfStudentDetailView.as_view()),
    path('dashboard/', DashboardView.as_view())
]
