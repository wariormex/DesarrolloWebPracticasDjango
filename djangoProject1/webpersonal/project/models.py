from turtle import title
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="project")
    url = models.URLField(verbose_name="URL")
    
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de modificacion")
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        
        ordering = ['-created']
    
    def __str__(self):
        return self.title
