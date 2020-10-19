from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.http import HttpResponse
from .models import UserRegister


# Create your views here.

def login(request):
	form=RegisterForm(request.POST)
	if form.is_valid():
		form.save()
		
		return HttpResponse('Image Uploaded..')
	form=RegisterForm()
	return render(request,'UserAccount/login.html',{'fields':form})



def show(request):
	data=UserRegister.objects.all()
	return render(request,'UserAccount/show.html',{'data':data})

def update(request,id):
	data=RegisterForm.objects.get(id=id)
	if request.method=='POST':
		form=RegisterForm(request.POST, instance=data)
		if form.is_valid():
			form.save()
	form =RegisterForm(instance=data)
	return render(request,'UserAccount/update.html',{"form":form,
		"data":data})

def delete(request,id):
	ob=UserRegister.objects.get(id=id)
	if request.method=='POST':
		ob.delete()
		
		return redirect('/show')
	return render(request,'UserAccount/message.html', {"info":ob})



