from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, VisitorLog
from .serializers import EmployeeSerializer, VisitorLogSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'Please provide username, email, and password'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        token = Token.objects.create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class VisitorLogListCreateAPIView(generics.ListCreateAPIView):
    queryset = VisitorLog.objects.all()
    serializer_class = VisitorLogSerializer
    permission_classes = [IsAuthenticated]

class VisitorLogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VisitorLog.objects.all()
    serializer_class = VisitorLogSerializer
    permission_classes = [IsAuthenticated]
