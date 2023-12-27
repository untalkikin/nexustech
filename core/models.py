from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Mata:
        verbose_name = "contenido"
        verbose_name_plural = "contenidos"
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class PictureUS(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título de imagen")
    image = models.ImageField(verbose_name="Imagen", upload_to="picturesUS")
    linkFb = models.CharField(max_length=300, verbose_name="Enlace de facebook")
    linkIg = models.CharField(max_length=300, verbose_name="Enlace de Instagram")
    linkX = models.CharField(max_length=300, verbose_name="Enlace de X")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "uspicture"
        verbose_name_plural = "uspcitures"
        ordering = ['-created']
        
    def __str__(self):
        return self.title 
    
class Partner(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del partnet")
    profilepicture = models.ImageField(verbose_name="Imagen", upload_to="profilepic")
    since = models.DateField(verbose_name="Fecha de alta del partner")
    position = models.CharField(max_length=300, verbose_name="Puesto del partner")
    contract = models.CharField(max_length=200, verbose_name="Nombre del partnet")
    description = models.TextField(verbose_name="Descripcion del partner")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partners"
        ordering = ['-created']
        
    def __str__(self):
        return self.name
    
    