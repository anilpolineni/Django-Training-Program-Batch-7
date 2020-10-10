from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'FirstApp/home.html')

def table(request):
	return render(request,'FirstApp/table.html')

def forms(request):
	return render(request,'FirstApp/forms.html')

def names(request,n):
	return render(request,'FirstApp/names.html',{'name':n})

def numbers(request,num):
	n=[]
	for i in range(1,num+1):
		n.append(i)

	return render(request,'FirstApp/numbers.html',{'num':n})

def register(request):
	if request.method=='POST':
		uname=request.POST['name']
		uemail=request.POST['email']
		ubranch=request.POST['branch']
		umobile=request.POST['mobile']
		ugender=request.POST['gender']
		#return HttpResponse('User Data Registered...')
		return render(request,'FirstApp/data.html',{'name':uname,'email':uemail,
			'branch':ubranch,'mobile':umobile,'gender':ugender})
	return render(request,'FirstApp/register.html')