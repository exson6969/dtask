from django.urls import path
from .views import UserRegistrationView, EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView, VisitorLogListCreateAPIView, VisitorLogRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
    path('visitor-logs/', VisitorLogListCreateAPIView.as_view(), name='visitor-log-list-create'),
    path('visitor-logs/<int:pk>/', VisitorLogRetrieveUpdateDestroyAPIView.as_view(), name='visitor-log-detail'),
]
