from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request,'boot/home.html')

def register(request):
	return render(request,'boot/register.html')