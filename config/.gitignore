from django.db import models


class Jogo(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    ano_lancamento = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo