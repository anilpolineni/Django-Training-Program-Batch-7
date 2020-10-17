from django.shortcuts import render
from FirstApp.forms import MoviesForm
from django.http import HttpResponse
from FirstApp.models import Movies
# Create your views here.
def register(request):
	form=MoviesForm(request.POST)
	if form.is_valid():
		form.save()
		return HttpResponse('Registered Successfully')
	
	form=MoviesForm()
	return render(request,'FirstApp/register.html',{'form':form})

def showdata(request):
	data=Movies.objects.all()
	return render(request,'FirstApp/showdata.html',{'data':data})