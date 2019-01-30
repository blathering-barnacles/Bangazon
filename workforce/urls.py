from django.urls import path

from workforce import views
from . import views

app_name = 'workforce'
urlpatterns = [
    path('training/', views.trainingList, name='training'),
    path('addtraining/', views.newTraining, name='addTraining'),
	path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
    path('addEmployee/', views.addEmployee, name='addEmployee')
]