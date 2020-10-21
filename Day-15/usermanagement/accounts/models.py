from django.db import models

from django.contrib.auth.models import User

from PIL import Image

# Create your models here.


class UserProfile(models.Model):
	gen=(('male','Male'),('female','Female'))
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="pics/")
	gender=models.CharField(max_length=10,choices=gen)
	dob=models.DateField(null=True)
	mobileno=models.CharField(max_length=10)
	address=models.TextField()

