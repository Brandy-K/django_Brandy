from django.db import models

# Create your models here.


class Students(models.Model):
    nom = models.CharField(max_length=20)
    cognom1 = models.CharField(max_length=20)
    cognom2 = models.CharField(max_length=20)
    correu = models.CharField(max_length=50)
    curs = models.CharField(max_length=10)
    moduls_matriculats = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom} {self.cognom1} {self.cognom2}"


class Teachers(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=20)
    cognom = models.CharField(max_length=20)
    edat = models.IntegerField(max_length=20)
    rol = models.CharField(max_length=20)
    curs = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom} {self.cognom} {self.curs}"

