from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):

	return HttpResponse("This is My First Django Project")

def hi(request):
	name="APSSDC"
	return HttpResponse('<h1>Hi Hello This is {} </h1>'.format(name))

def names(request,n):
	return HttpResponse('<h1>Welcome to {} </h1>'.format(n))

def roll(request,r):
	return HttpResponse('My Roll Number is {}'.format(r))

def data(request,name,roll):
	return HttpResponse('My Name is {} and my roll number is {}'.format(name,roll))