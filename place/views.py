from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  User.objects.all()
    permission_classes = [IsAuthenticated]