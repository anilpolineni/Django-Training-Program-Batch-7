from django.db import models

# Create your models here.
class Employee(models.Model):
	Sno=models.IntegerField()
	FirstName=models.TextField(max_length=50)
	LastName=models.TextField(max_length=50)
	Email=models.EmailField(max_length=50)

	def __str__(self):
		return self.FirstName+" "+self.Email
