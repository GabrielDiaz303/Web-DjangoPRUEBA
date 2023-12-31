from django.db import models

# Create your models here.

class Project (models.Model):
    title = models.CharField(max_length=20, verbose_name = 'titulo')
    description = models.TextField(verbose_name = 'descripción')
    image = models.ImageField(verbose_name = 'imagen', upload_to="projects")
    link = models.URLField(verbose_name= "enlace", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'actualizado')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']  #Ordenar de forma descendente.
        
        