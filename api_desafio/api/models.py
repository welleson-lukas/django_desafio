from django.db import models

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.nome

