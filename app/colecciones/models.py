from django.db import models

# Modelo examenes

class Examen(models.Model):
    codigo = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.nombre

class Diagnostico(models.Model):
    codigo = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class Medicina(models.Model):
    codigo = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre