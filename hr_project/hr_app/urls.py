from django.urls import path
from .views import (
    EmployeeListCreateView, EmployeeDetailView,
    PerformanceReviewListCreateView, PerformanceReviewDetailView,
    RegisterView, LoginView
)

urlpatterns = [
    path('employees', EmployeeListCreateView.as_view()),
    path('employees/<int:pk>', EmployeeDetailView.as_view()),

    path('reviews', PerformanceReviewListCreateView.as_view()),
    path('reviews/<int:pk>', PerformanceReviewDetailView.as_view()),

    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
]
