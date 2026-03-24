from rest_framework import serializers
from .models import Estudantes, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
        class Meta:
                model = Estudantes
                fields = '__all__'
                
class CursoSerializer(serializers.ModelSerializer):
        class Meta:
                model = Curso
                fields = '__all__'
                
class MatriculaSerializer(serializers.ModelSerializer):
        class Meta:
                model = Matricula
                fields = '__all__'
