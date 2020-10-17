from django.db import models

# Create your models here.

class UserRegister(models.Model):
	fullname=models.CharField(max_length=100)
	mailid=models.EmailField(max_length=100)
	pwd=models.CharField(null=True, max_length=20)
	#image=models.FileField(upload_to='profilepics/')

	def __str__(self):
		return self.fullname+" "+self.mailid