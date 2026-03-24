from django.shortcuts import render
from rest_framework import viewsets
from .models import Estudantes, Curso, Matricula
from .serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

# Create your views here.
class EstudanteViewSet(viewsets.ModelViewSet):
        queryset = Estudantes.objects.all()
        serializer_class = EstudanteSerializer
        
class CursoViewSet(viewsets.ModelViewSet):
        queryset = Curso.objects.all()
        serializer_class = CursoSerializer
        
class MatriculaViewSet(viewsets.ModelViewSet):
        queryset = Matricula.objects.all()
        serializer_class = MatriculaSerializer