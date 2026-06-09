from django.db import models
class CoffeReporte(models.Model):
    titulo = models.CharField(max_length=20);
    csv=models.FileField(upload_to="csv/")
    
    def __str__(self):
        return self.titulo
