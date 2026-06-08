from django.db import models


class Mensagem(models.Model):
    titulo = models.CharField(max_length=120)
    conteudo = models.TextField(max_length=600)
    criada_em = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=80)
    
    class Meta:
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo
