from django.urls import path

from workforce import views
from . import views

app_name = 'workforce'
urlpatterns = [
    path('training/', views.trainingList, name='training'),
	path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
    path('addtraining/', views.newTraining, name='addTraining')
]




