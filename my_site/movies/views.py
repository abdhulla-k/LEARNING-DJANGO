from django.shortcuts import render
from .models import MoviesData
from rest_framework import viewsets
from .serializers import ModelSerializer

# Create your views here.

class MovieViewSet( viewsets.ModelViewSet ):
    queryset = MoviesData.objects.all()
    serializer_class = ModelSerializer