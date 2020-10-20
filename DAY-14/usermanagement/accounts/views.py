from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from .models import UserProfile

from django.contrib import messages

from usermanagement import settings

from django.core.mail import send_mail

# Create your views here.


def home(request):
	return render(request,'accounts/home.html')


def register(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		uname=request.POST['uname']
		em=request.POST['emailid']
		im=request.FILES['image']
		pwd=request.POST['pswd']
		user=User.objects.create_user(first_name=fname,last_name=lname,
			username=uname,email=em,password=pwd)
		UserProfile.objects.create(user=user,image=im)
		sub="user logins"
		body="Welcome to our project \n This Your UserName"+uname+ "\n Ths is Your Password"+pwd
		recever=em
		sender=settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[recever])
		messages.success(request,'%s is successully Registred..!'%(uname))
		return redirect('signin')
	else:
		return render(request,'accounts/register.html')


def signin(request):
	return render(request,'accounts/signin.html')