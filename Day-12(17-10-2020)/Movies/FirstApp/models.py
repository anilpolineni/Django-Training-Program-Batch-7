from django.db import models

# Create your models here.
class Movies(models.Model):
	moviename=models.CharField(max_length=100)
	heroname=models.CharField(max_length=50)
	heroinname=models.CharField(max_length=50)
	director=models.CharField(max_length=50)
	reldate=models.DateField(null=True)
