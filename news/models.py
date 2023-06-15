from django.db import models

# Create your models here.

class Noticia(models.Model):
    nome_noticia = models.CharField(max_length=200)
    resumo_noticia = models.CharField(max_length=200)
    url_site = models.TextField(default="")

    def __str__(self):
        return self.nomeDaNoticia



    
   
