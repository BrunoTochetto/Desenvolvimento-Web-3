from django.db import models

class Estudantes(models.Model):
        nome_completo = models.CharField(max_length=200)
        email = models.EmailField()
        telefone = models.CharField(max_length=20)
        data_cadastro = models.DateTimeField(auto_now_add=True)
        matricula_id = models.IntegerField(auto_created=True, null=True)
        
        def __str__(self):
                return self.nome_completo

class Matricula(models.Model):
        valor = models.CharField(max_length=10)
        data_cadastro = models.DateTimeField(auto_now_add=True)
        estudante = models.ForeignKey(to=Estudantes, on_delete=models.CASCADE, null=True, unique=True)
        
        def __str__(self):
                return self.valor

class Curso(models.Model):
        nome = models.CharField(max_length=200) 
        codigo = models.CharField(max_length=20)
        email_contato = models.EmailField()
        data_cadastro = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
                return self.codigo
        
