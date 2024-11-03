from django.db import models

class ListModel(models.Model):
	titulo = models.CharField(max_length=100)