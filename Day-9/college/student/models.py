from django.db import models

# Create your models here.

# custom table

class Student(models.Model):
	rollno=models.CharField(max_length=10)
	name=models.CharField(max_length=20)
	dept=models.CharField(max_length=30)
	mobileno=models.CharField(max_length=10)
	age=models.IntegerField()
	pincode=models.CharField(max_length=6)

	def __str__(self):
		return self.rollno+" "+self.dept


