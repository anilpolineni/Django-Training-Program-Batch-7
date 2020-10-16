from django.urls import path

from.views import home,addstudent,showdata,updatestudent,deletestudent

urlpatterns = [
	path('',home,name="home"),
	path('addstudent',addstudent,name="addstudent"),
	path('showdata',showdata,name="showdata"),
	path('updatestudent/<int:id>',updatestudent,name="updatestudent"),
	path('deletestudent/<int:id>',deletestudent,name="deletestudent"),
	]