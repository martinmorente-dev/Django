from django.db import models
from django.contrib.auth.models import User as AuthUser

class UserProfile(models.Model):
	user = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)

class ListModel(models.Model):
	titulo = models.CharField(max_length=100)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


# Nota: Cuando estamos haciendo relaciones la tabla user 
# tiene que ir primero porque si no la tabla no es capaz 
# de encontrarlo ya que no está creado.