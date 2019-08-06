# Posts models

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)  # Va a ser un valor en blanco, Por defecto tiene un valor null
    created = models.DateField(auto_now_add=True)   # El argumento dice que cuando se cree la instancia por defecto le dara la fecha de creación
    modified = models.DateField(auto_now=True)  # La fec1ha en la que se editó por ultima vez
    county = models.CharField(max_length=40,blank=True)

    def __str__(self):
        return self.email