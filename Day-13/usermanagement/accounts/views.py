from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request,'accounts/home.html')


def register(request):
	return render(request,'accounts/register.html')


def signin(request):
	return render(request,'accounts/signin.html')