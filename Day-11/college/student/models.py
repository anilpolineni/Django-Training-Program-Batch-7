from django.db import models

# Create your models here.

# custom table

class Student(models.Model):
	rollno=models.CharField(max_length=10)
	name=models.CharField(max_length=20)
	email=models.EmailField(max_length=30)
	dept=models.CharField(max_length=30)
	age=models.IntegerField()
	mobileno=models.CharField(max_length=10)
	
	def __str__(self):
		return self.rollno+" "+self.dept


