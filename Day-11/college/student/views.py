from django.shortcuts import render

from django.http import HttpResponse

from.models import Student

# Create your views here.

def home(request):
	return render(request,'student/home.html')


def addstudent(request):
	if request.method=="POST":
		roll=request.POST['rollno']
		na=request.POST['name']
		em=request.POST['emailid']
		dpt=request.POST['dept']
		ag=request.POST['age']
		mb=request.POST['mobileno']
		Student.objects.create(rollno=roll,name=na,email=em,dept=dpt,age=ag,mobileno=mb)
		return HttpResponse('successfully Added..!')
	else:
		return render(request,'student/addstudent.html')


def showdata(request):
	data=Student.objects.all()
	context={'data':data}
	return render(request,'student/showdata.html',context)


def updatestudent(request,id):
	datas=Student.objects.get(id=id)
	if request.method=="POST":
		datas.rollno=request.POST['rollno']
		datas.name=request.POST['name']
		datas.email=request.POST['emailid']
		datas.dept=request.POST['dept']
		datas.age=request.POST['age']
		datas.mobileno=request.POST['mobileno']
		datas.save()
		return HttpResponse('successfully updated..!')
	else:
		return render(request,"student/updatestudent.html",{"data":datas})


def deletestudent(request,id):
	obj=Student.objects.get(id=id)
	obj.delete()
	return HttpResponse('successfully deleted')