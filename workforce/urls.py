from django.urls import path

from workforce import views
from . import views

app_name = 'workforce'

urlpatterns = [
	path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
]
