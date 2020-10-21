from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from .models import UserProfile

from django.contrib import messages

from usermanagement import settings

from django.core.mail import send_mail

from django.contrib.auth import authenticate,login,logout

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
		# sub="user logins"
		# body="Welcome to our project \n This Your UserName"+uname+ "\n Ths is Your Password"+pwd
		# recever=em
		# sender=settings.EMAIL_HOST_USER
		# send_mail(sub,body,sender,[recever])
		messages.success(request,'%s is successully Registred..!'%(uname))
		return redirect('signin')
	else:
		return render(request,'accounts/register.html')


def signin(request):
	if request.method=="POST":
		un=request.POST['uname']
		pwd=request.POST['pswd']
		user=authenticate(username=un,password=pwd)
		if user:
			login(request,user)
			messages.success(request,"%s is logged successully..!"%(un))
			return redirect('/')
		else:
			messages.error(request,'Invalid UserName or Password')
			return render(request,'accounts/signin.html')
	else:
		return render(request,'accounts/signin.html')


def changepassword(request):
	if request.method=="POST":
		old=request.POST['oldpwd']
		new=request.POST['newpwd']
		con=request.POST['conpwd']
		if new==con:
			user=User.objects.get(username__exact=request.user.username)
			user.set_password(new)
			user.save()
			messages.info(request,'password is successully updated..!')
			return redirect('/')
		else:
			messages.error(request,"password dosen't match")
			return render(request,'accounts/changepassword.html')
	else:
		return render(request,'accounts/changepassword.html')



def profile(request):
	user=User.objects.get(id=request.user.id)
	pro=UserProfile.objects.get(user=user)
	context={'user':user,'pro':pro}
	return render(request,'accounts/profile.html',context)




def signout(request):
	logout(request)
	return redirect('/')