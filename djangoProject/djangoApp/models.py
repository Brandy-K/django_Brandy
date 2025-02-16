from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username
